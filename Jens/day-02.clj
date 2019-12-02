(def input (as-> "inputs/day-02.txt" x
             (slurp x)
             (clojure.string/trim-newline x)
             (clojure.string/split x #",")
             (map #(Integer/parseInt %) x)))

(defn add-and-store [tape pos1 pos2 store]
  (concat (take store tape)
          [(+ (nth tape pos1)
              (nth tape pos2))]
          (drop (inc store) tape)))

(defn multiply-and-store [tape pos1 pos2 store]
  (concat (take store tape)
          [(* (nth tape pos1)
              (nth tape pos2))]
          (drop (inc store) tape)))

(defn computer [tape noun verb]
  (concat (take 1 tape)
          [noun]
          [verb]
          (drop 3 tape)))

(defn run-until-stop [computer]
  (loop [pointer 0
         tape computer]
    (let [next-index (+ pointer 4)
          [opcode p1 p2 p3] (drop pointer tape)]
      (case opcode
        1 (recur next-index
                 (add-and-store tape p1 p2 p3))
        2 (recur next-index
                 (multiply-and-store tape p1 p2 p3))
        99 (first tape)))))

;; PART ONE
(println (str "Part one: The value of index 0 when the program stops is " (run-until-stop (computer input 12 2))))

;; PART TWO

(def desired-result 19690720)

(def part-2-answer
  (loop [n-val 0
         v-val 0]
    (let [result (run-until-stop (computer input n-val v-val))
          reset  (= 99 n-val)]
      (if (= result desired-result)
        (+ (* 100 n-val)
           v-val)
        (recur (if reset
                 0
                 (inc n-val))
               (if reset
                 (inc v-val)
                 v-val))))))

(println (str "Part two: The input pair that produces the result " desired-result " is " part-2-answer))
