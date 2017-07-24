(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)


(define (sign x)
  (cond
        ((> x 0) 1)
        ((= x 0) 0)
        ((< x 0) -1)
  )
)


(define (square x) (* x x))
(define (odd? x) (= (remainder x 2) 1))
(define (even? x) (= (remainder x 2) 0))

(define (pow b n)
  (cond
        ((= n 0) 1)
        ((even? n) (square (pow b (/ n 2))))
        (else (* b (pow b (- n 1))))
  )
)


(define (ordered? s)
    (if (null? (cdr s))
        True
        (and (<= (car s) (cadr s)) (ordered? (cdr s)))
    )
)


(define (dotted? s) (and (pair? s)
                    (not (or (pair? (cdr s))
                             (null? (cdr s))))))
(define (nodots s)
      (cond ((null? s) s)
          ((dotted? s) (list (nodots (car s)) (cdr s)))
          ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
          (else s))
)


; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) false)
          ((= (car s) v) True)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return len(s) == 0
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((= (car s) v) s)
          ((> (car s) v) (cons v s))
          (else (cons (car s) (add (cdr s) v)))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((contains? s (car t)) (cons (car t) (intersect s (cdr t))))
          (else (intersect s (cdr t))
          )))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((contains? s (car t)) (union s (cdr t)))
          (else (union (add s (car t)) (cdr t))
          )))


