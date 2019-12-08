(refer 'aoc.2019.computer)

(def input (as-> "inputs/day-02.txt" x
             (slurp x)
             (clojure.string/trim-newline x)
             (clojure.string/split x #",")
             (map #(Integer/parseInt %) x)))

;; PART ONE

(def part-1 (first (:memory (run-program (computer input {:noun 12 :verb 2})))))

(printf "Part one: The value in index 0 after running the program is %s\n" part-1)

;; PART TWO

(def desired-result 19690720)
(def noun-verb-combos (for [n (range 0 100) v (range 0 100)] [n v]))

(def part-2
  (let [runs           (map #(run-program (computer input {:noun (first %) :verb (second %)})) noun-verb-combos)
        successful-run (first (drop-while #(not= desired-result (first (:memory %))) runs))]
    (+ (* 100 (:noun successful-run)) (:verb successful-run))))

(printf "Part two: The noun-verb combination that produces the output %s is %s" desired-result part-2)
