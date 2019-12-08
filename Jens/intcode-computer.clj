(ns aoc.2019.computer)

(defn get-value [mem x p-mode]
  (case p-mode
    0 (nth mem x)
    1 x))

(defn add-and-store
  ([c params]
   (add-and-store c params [0 0]))
  ([c [p1 p2 s] [m1 m2 & _]]
   (assoc-in c [:memory s] (+ (get-value (:memory c) p1 m1)
                              (get-value (:memory c) p2 m2)))))

(defn multiply-and-store
  ([c params]
   (multiply-and-store c params [0 0]))
  ([c [p1 p2 s] [m1 m2 & _]]
   (assoc-in c [:memory s] (* (get-value (:memory c) p1 m1)
                              (get-value (:memory c) p2 m2)))))

(defn output-value
  ([c [p] [m]]
   (output-value c false))
  ([c [p] [m] print?]
   (let [v (get-value (:memory c) p m)]
     (do (if print? (println v))
         (update c :outputs conj v)))))

(defn store-input
  [c [p] & _]
  (-> c
      (assoc-in [:memory p] (first (:inputs c)))
      (update :inputs #(drop 1 %))))

(defn stop [c]
  (assoc c :running false))

(def instruction-set
  {1  [add-and-store 3]
   2  [multiply-and-store 3]
   3  [store-input 1]
   4  [output-value 1]
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
        parameters  (take (second instruction) (drop (inc pointer) (:memory c)))
        modes       (parameter-modes opcode (count parameters))]
    (-> c
        ((first instruction) parameters)
        (update :pointer + (inc (count parameters))))))

(defn run-program [computer]
  (first (drop-while :running (iterate perform-next-instruction computer))))
