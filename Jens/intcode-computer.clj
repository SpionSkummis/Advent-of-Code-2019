(ns aoc.2019.computer)

(defn get-value [mem x p-mode]
  (case p-mode
    0 (nth mem x)
    1 x))

(defn add-and-store
  [c [p1 p2 s] [m1 m2 & _]]
  (assoc-in c [:memory s] (+ (get-value (:memory c) p1 m1)
                             (get-value (:memory c) p2 m2))))

(defn multiply-and-store
  [c [p1 p2 s] [m1 m2 & _]]
  (assoc-in c [:memory s] (* (get-value (:memory c) p1 m1)
                             (get-value (:memory c) p2 m2))))

(defn output-value
  ([c p m]
   (output-value c p m false))
  ([c [p] [m] print?]
   (let [v (get-value (:memory c) p m)]
     (do (if print? (println v))
         (update c :outputs conj v)))))

(defn store-input
  [c [p] & _]
  (-> c
      (assoc-in [:memory p] (first (:inputs c)))
      (update :inputs #(drop 1 %))))

(defn jump-if-true
  [c [p1 p2] [m1 m2]]
  (if (not (zero? (get-value (:memory c) p1 m1)))
    (assoc c :pointer (- (get-value (:memory c) p2 m2) 3))
    c))

(defn jump-if-false
  [c [p1 p2] [m1 m2]]
  (if (zero? (get-value (:memory c) p1 m1))
    (assoc c :pointer (- (get-value (:memory c) p2 m2) 3))
    c))

(defn less-than
  [c [p1 p2 s] [m1 m2 _]]
  (let [r (if (< (get-value (:memory c) p1 m1) (get-value (:memory c) p2 m2))
            1 0)]
    (assoc-in c [:memory s] r)))

(defn equals
  [c [p1 p2 s] [m1 m2 _]]
  (let [r (if (= (get-value (:memory c) p1 m1) (get-value (:memory c) p2 m2))
            1 0)]
    (assoc-in c [:memory s] r)))

(defn stop [c & _]
  (assoc c :running false))

(def instruction-set
  {1  [add-and-store 3]
   2  [multiply-and-store 3]
   3  [store-input 1]
   4  [output-value 1]
   5  [jump-if-true 2]
   6  [jump-if-false 2]
   7  [less-than 3]
   8  [equals 3]
   99 [stop 0]})

(defn computer [tape settings]
  (conj {:pointer 0
         :memory (if (contains? settings :noun)
                   (into [] (concat (take 1 tape)
                                    [(:noun settings)]
                                    [(:verb settings)]
                                    (drop 3 tape)))
                   tape)
         :running true
         :noun (nth tape 1)
         :verb (nth tape 2)
         :inputs []
         :outputs []}
        settings))

(defn extract-parameters [mem p n]
  (take n (drop (inc p) mem)))

(defn parameter-modes [x n]
  (take n (concat
           (loop [inm  (quot x 100)
                  outm []]
             (if (zero? inm)
               outm
               (recur (quot inm 10)
                      (conj outm (mod inm 10)))))
           (repeat 0))))

(defn perform-next-instruction [c]
  (let [pointer     (:pointer c)
        opcode      (nth (:memory c) pointer)
        instruction (get instruction-set (mod opcode 100))
        parameters  (extract-parameters (:memory c) pointer (second instruction))
        modes       (parameter-modes opcode (count parameters))]
    (-> c
        ((first instruction) parameters modes)
        (update :pointer + (inc (count parameters))))))

(defn run-program [computer]
  (first (drop-while :running (iterate perform-next-instruction computer))))
