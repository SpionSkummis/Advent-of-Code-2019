(def input (->> "inputs/day-01.txt"
                slurp
                clojure.string/split-lines
                (map #(Integer/parseInt %))))

;; PART 1

(defn fuel-req [x]
  (- (quot x 3) 2))

(def module-fuel (map fuel-req input))
(println (str "Part 1: The required fuel is " (reduce + module-fuel)))

;; PART 2

(def additional-fuel (map #(iterate fuel-req %) module-fuel))

(def total-fuel (->> additional-fuel
                  (map (partial take-while #(not (neg? %))))
                  (map (partial reduce +))))

(println (str "Part 2: The required fuel is " (reduce + total-fuel)))
