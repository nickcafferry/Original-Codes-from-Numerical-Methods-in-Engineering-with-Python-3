
# Welcome to Jupyter!


```python
function [x,det] = gaussElimin(a,b)
n = length(b);
for k = 1:n-1
    for i = k+1:n
        if a(i,k)~=0
            lam = a(i,k)/a(k,k);
            a(i,k+1:n) = a(i,k+1:n)-lam*a(k,K+1:n);
            b(i) = b(i)-lam*b(k);
        end
    end
end
det = prod(diag(a));
for k = n:-1:1
    b(k) = (b(k)-a(k,k+1:n)*b(k+1:n))/a(k,k);
end
x = b;
```
