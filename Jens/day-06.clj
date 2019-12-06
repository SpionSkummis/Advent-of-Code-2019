(def input (as-> "inputs/day-06.txt" $
             (slurp $)
             (re-seq #"(\w{3})\)(\w{3})" $)
             (map #(drop 1 %) $)))

(def test-input [["COM" "B"]
                 ["B" "C"]
                 ["C" "D"]
                 ["D" "E"]
                 ["E" "F"]
                 ["B" "G"]
                 ["G" "H"]
                 ["D" "I"]
                 ["E" "J"]
                 ["J" "K"]
                 ["K" "L"]
                 ["K" "YOU"]
                 ["I" "SAN"]])

(defn node [parent children]
  {:parent parent
   :children children})

(defn find-parent [list-of-bodies id]
  (first (some #(when (= id (second %)) %) list-of-bodies)))

(defn list-children [list-of-bodies id]
  (seq (map second (filter #(= id (first %)) list-of-bodies))))

(defn make-node [list-of-bodies id]
  [id (node (find-parent list-of-bodies id) (list-children list-of-bodies id))])

(defn make-tree [list-of-bodies]
  (as-> list-of-bodies $
    (flatten $)
    (distinct $)
    (mapcat make-node (repeat list-of-bodies) $)
    (apply hash-map $)))

(defn find-root [tree]
  (flatten (remove #(some? (:parent (second %))) tree)))

(defn search-up-branch
  ([tree start]
   (search-up-branch tree start (first (find-root tree))))
  ([tree start target]
   (loop [curr (get tree start)
          steps []]
     (if-let [parent (:parent curr)]
       (if (= parent target)
         (conj steps parent)
         (recur (get tree parent)
                (conj steps parent)))
       nil))))

(def orbit-tree (make-tree input))

(def part-1 (reduce #(+ %1 (count %2)) 0
                    (map #(search-up-branch orbit-tree % "COM") (keys orbit-tree))))

(printf "\nPart one: The total number of orbits is %s" part-1)

(defn first-common-node [branch-a branch-b]
  (reduce #(if (some (fn [x] (= %2 x)) branch-b)
             (reduced %2)
             %1) nil branch-a))

(def part-2 (let [branch-to-you   (search-up-branch orbit-tree "YOU")
                  branch-to-santa (search-up-branch orbit-tree "SAN")
                  rest-of-trunk (search-up-branch orbit-tree (first-common-node branch-to-you branch-to-santa))]
              (- (+ (count branch-to-you)
                    (count branch-to-santa))
                 (* (count rest-of-trunk) 2)
                 2)))

(printf "\nPart two: We are required to make %s jumps in order to reach the same orbit as Santa" part-2)

