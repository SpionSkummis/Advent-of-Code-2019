(def password-range (range 147981 (inc 691423)))

(defn split-into-digits [x]
  (loop [v x
         l []]
    (if (< v 10)
      (reverse (conj l v))
      (recur (quot v 10)
             (conj l (mod v 10))))))

(defn increasing? [x]
  (some? (reduce #(if (<= %1 %2) %2 (reduced nil)) (split-into-digits x))))

(defn repeating-digits [x]
  (map first (re-seq #"(\d)\1+" (str x))))

;; PART ONE

(defn keep-condition-1 [x]
  (and (increasing? x)
       (repeating-digits x)))

(def part-1 (count (filter keep-condition-1 password-range)))
(printf "Part one: There are %s possible candidates\n" part-1)

;; PART TWO

(defn keep-condition-2 [x]
  (and (increasing? x)
       (some #(= 2 (count %)) (repeating-digits x))))

(def part-2 (count (filter keep-condition-2 password-range)))
(printf "Part two: There are %s possible candidates\n" part-2)
