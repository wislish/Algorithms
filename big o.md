# Big O
In the industry world, it means **offer the tightest description, not only the upper bound.**

**Space Complexity**: pay attention to `simultaneously`
 
**Add vs Multi Complexity** ![](/media/15009629860384.jpg)


---- 
## Examples and Answers

![](/media/15009628672720.jpg)

1. 求和公式：$$ n-1 + n-2 + ... + 1 = \frac{n(n-1)}{2} $$ 因此O($n^2$)

2. 从n个中取出不同的两个元素，忽略顺序，组合数：$C{n \choose 2}$

![](/media/15009643115731.jpg)
> ignore constant times

----
![](/media/15009653094780.jpg)
----
![](/media/15009658063652.jpg)
> difference between length of array and len of each string.

----

* Recursive Pattern

![](/media/15009684740082.jpg)

**Or, we can think about it recursively,**

![](/media/15009686093394.jpg)

$O(2^{log N} = N)$

----
![](/media/15009694922450.jpg)
----
> Most Difficult !!!

![](/media/15009711939092.jpg)

![](/media/15009721413368.jpg)

1. 分为两步计算，一是permuatation这个函数被调用了多少次，二是每次调用的时间复杂度是多少。
2. 如果把整个permutation看成是一棵树的话，每个叶结点 (leaves)都是一种排列形式。那么，这棵树的每一条路径都经过了n次调用，一共就是$O(n*n!)$。
3. 每一次调用，操作的时间都跟n是正相关的，$O(n)$。因为，rem, prefix, str.charat(i)的长度之和斗士n。
4. 因此，整体时间复杂度是 $O(n^2 * n!)$

----
![](/media/15010545295777.jpg)
> 我们可以把这个例子和上个例子结合起来看，都是对递归的时间复杂度的测算。我们首先都是数函数被call了多少次。然后乘以每一次call的时间。
> Example 13中，fib()一共被调用了$2^n-1$次（粗略），我们可以通过如下的例子来帮助我们分析。

```java
int f(int n ){
    if (n <=1){
        return 1;
    }
    return f(n-1) + f(n-1)
}

```
![](/media/15010551181312.jpg)

----
下面的几个例子可以进一笔温习一下。

![](/media/15010552485803.jpg)
----
![](/media/15010556571159.jpg)
![](/media/15010556863046.jpg)
----
![](/media/15010564437797.jpg)
![](/media/15010564657699.jpg)



