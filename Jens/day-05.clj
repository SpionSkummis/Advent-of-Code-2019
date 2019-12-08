(refer 'aoc.2019.computer)

(def input (as-> "inputs/day-05.txt" $
             (slurp $)
             (clojure.string/trim-newline $)
             (clojure.string/split $ #",")
             (map #(Integer/parseInt %) $)
             (into [] $)))

;; PART ONE

(def result-1 (run-program (computer input {:inputs [1]})))

(def part-1 (last (:outputs result-1)))

(printf "\nPart one: The diagnostics code is %s" part-1)

;; PART TWO

(def result-2 (run-program (computer input {:inputs [5]})))

(def part-2 (last (:outputs result-2)))

(printf "\nPart two: The diagnostic code is %s" part-2)
