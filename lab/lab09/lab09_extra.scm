;; Extra Scheme Questions ;;

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((= 0 (min a b)) (max a b))
        ((= 1 (min a b)) 1)
        ((= 0 (remainder (max a b) (min a b))) (min a b))
        (else (gcd (min a b) (remainder (max a b) (min a b)))))
)


; Q10

(define (num-leaves tree)
  (cond ((null? tree) 0)
        ((leaf? tree) 1)
        (else (+ (num-leaves (right tree)) (num-leaves (left tree))))
  )
)

; Q11
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)


; Binary Tree ADT
(define (make-btree entry left right)
  (cons entry (cons left right)))

(define (entry tree)
  (car tree))

(define (left tree)
  (car (cdr tree)))

(define (right tree)
  (cdr (cdr tree)))

(define (leaf? tree) (and (null? (left tree)) (null? (right tree))))

(define test-tree
  (make-btree 2
              (make-btree 1
                          nil
                          nil)
              (make-btree 4
                          (make-btree 3
                                      nil
                                      nil)
                          nil)))

; test-tree:
;     2
;    / \
;   1   4
;      /
;     3
