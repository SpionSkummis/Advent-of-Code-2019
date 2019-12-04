(def input (as-> "inputs/day-03.txt" $
             (slurp $)
             (clojure.string/split-lines $)
             (map #(clojure.string/split % #",") $)))

(defn wire [directions]
  (map #(vector (first %) (Integer/parseInt (subs % 1))) directions))

(defn inc-x [[steps pos]]
  [(inc steps) [(inc (first pos)) (last pos)]])
(defn dec-x [[steps pos]]
  [(inc steps) [(dec (first pos)) (last pos)]])
(defn inc-y [[steps pos]]
  [(inc steps) [(first pos) (inc (last pos))]])
(defn dec-y [[steps pos]]
  [(inc steps) [(first pos) (dec (last pos))]])

(defn move [position [direction distance]]
  (let [move-fn (case direction
                  \L dec-x \R inc-x
                  \D dec-y \U inc-y)]
    (take distance (drop 1 (iterate move-fn position)))))

(defn map-wire-positions [w]
  (reduce #(into %1 (move (last %1) %2)) [[0 [0 0]]] w))

(defn distance-to-port [p] (+ (Math/abs (first p))
                              (Math/abs (second p))))

(def wire-1 (map-wire-positions (wire (first input))))
(def wire-2 (map-wire-positions (wire (second input))))

(def intersections (set (remove #(= [0 0] %) (clojure.set/intersection (set (map second wire-1))
                                                                       (set (map second wire-2))))))

(def part-1 (first (sort (map distance-to-port intersections))))

(printf "Part 1: The closest intersection is located at a distance of %s" part-1)

(def wire-1-intersections (sort-by second (filter #(contains? intersections (second %)) wire-1)))
(def wire-2-intersections (sort-by second (filter #(contains? intersections (second %)) wire-2)))

(def part-2 (first (sort (map #(+ (first %1) (first %2)) wire-1-intersections wire-2-intersections))))

(printf "Part 2: The closest intersection is reached after %s steps" part-2)
