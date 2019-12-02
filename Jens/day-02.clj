(def input (as-> "inputs/day-02.txt" x
             (slurp x)
             (clojure.string/trim-newline x)
             (clojure.string/split x #",")
             (map #(Integer/parseInt %) x)))

(defn add-and-store [mem [p1 p2 store]]
  (assoc-in mem [store] (+ (nth mem p1) (nth mem p2))))

(defn multiply-and-store [mem [p1 p2 store]]
  (assoc-in mem [store] (* (nth mem p1) (nth mem p2))))

(defn stop [x _] false)

(def instruction-set
  {1  [add-and-store 3 :memory]
   2  [multiply-and-store 3 :memory]
   99 [stop 0 :running]})

(defn computer [tape noun verb]
  {:pointer 0
   :memory (into [] (concat (take 1 tape)
                            [noun]
                            [verb]
                            (drop 3 tape)))
   :running true
   :noun noun
   :verb verb})

(defn perform-next-instruction [computer]
  (let [pointer     (:pointer computer)
        opcode      (nth (:memory computer) pointer)
        instruction (get instruction-set opcode)
        parameters  (take (second instruction) (drop (inc pointer) (:memory computer)))
        target      (nth instruction 2)]
    (-> computer
        (update target #((first instruction) % parameters))
        (update :pointer #(+ % 1 (count parameters))))))

(defn run-program [computer]
  (first (drop-while :running (iterate perform-next-instruction computer))))

;; PART ONE

(def part-1 (first (:memory (run-program (computer input 12 2)))))

(printf "Part one: The value in index 0 after running the program is %s\n" part-1)

;; PART TWO

(def desired-result 19690720)
(def noun-verb-combos (for [n (range 0 100) v (range 0 100)] [n v]))

(def part-2
  (let [runs          (map #(run-program (computer input (first %) (second %))) noun-verb-combos)
        successful-run (first (drop-while #(not= desired-result (first (:memory %))) runs))]
    (+ (* 100 (:noun successful-run)) (:verb successful-run))))

(printf "Part two: The noun-verb combination that produces the output %s is %s" desired-result part-2)
