(def input (as-> "inputs/day-08.txt" $
             (slurp $)
             (clojure.string/trim-newline $)
             (map #(- (int %) 48) $)))

(defn build-layers [i h w]
  (loop [remaining i
         layers    []]
    (if (empty? remaining)
      layers
      (recur (drop (* h w) remaining)
             (conj layers (take (* h w) remaining))))))

(defn count-element [c e]
  (count (filter #(= e %) c)))

(def count-zeroes #(count-element % 0))

;; PART ONE

(def image-layers (build-layers input 25 6))

(def part-1 (let [correct-layer (reduce #(if (< (count-zeroes %1) (count-zeroes %2))
                                           %1 %2)
                                        image-layers)]
              (* (count-element correct-layer 1)
                 (count-element correct-layer 2))))

;; PART TWO

(defn final-pixel-color [pixel]
  (first (filter #(not= 2 %) pixel)))

(defn decode-image [layers]
  (let [pixels (apply map vector layers)]
    (map final-pixel-color pixels)))

(defn render-image [pixels w]
  (loop [remaining pixels
         image-rows []]
    (if (empty? remaining)
      image-rows
      (recur (drop w remaining)
             (conj image-rows (take w remaining))))))

(defn printable-image [image]
  (as-> image $
    (map #(apply str (replace {0 \. 1 \#} %)) $)
    (clojure.string/join "\n" $)))

(def part-2 (printable-image (render-image (decode-image image-layers) 25)))

(printf "Part two: The decoded image looks like \n%s" part-2)
