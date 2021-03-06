Week 1

1. 刷题方法：不要死磕一道题，几分钟没思路就直接看题解
2. 必要的代码可以背下来
3. 不必死背复杂度，但要理解
4. 记得处理边界值、起始/终止条件
5. 分析问题，找出规律，推导“最近重复子问题”
6. 升维思想、空间换时间

Week 2

1. 哈希表：把key通过哈希函数映射到某个位置，哈希函数的一个简单实现是把各字母的ascii相加
2. 哈希碰撞：两个key得到了相同的哈希函数值，解决的方法是接一个链表
3. map和set的区别：map是key-value对，key不重复；set没有value
4. 链表→（多个next指针）→树→（构成环）→图
5. 二叉搜索树：左子树＜根节点＜右子树，以此类推；其插入、查询等操作均为O(logN)；其中序遍历就是升序排列
6. 树的Demo：https://visualgo.net/zh/bst
7. 堆：可以直接找到最值的数据结构，任意节点>=其子节点；分为大顶堆、小顶堆（python里的heapq只有小顶堆）；堆属于完全二叉树
8. 二叉堆是插入/删除均为O(logN)，其中插入是先插到尾部然后依次向上交换，删除是将堆尾替换到该位置然后依次向下互换

Week 3

1. 递归模板：终结条件、处理当前层、进入下一层、清理当前层（较少见）
2. 分治：把问题拆解成两个（或多个）子问题，以此类推；相比递归，分治多了问题拆解和结果合并
3. 回溯：基于递归，采用试错的方法，错了就返回上一步继续

Week 4

1. 若DFS对应于二叉树的前中后序遍历，则BFS对应于层序遍历
2. 贪心算法只考虑当前，而动态规划能保存之前的运算结果并进行选择，即有回退功能
3. 一些题，关键在于如何证明贪心算法能得到全局最优
4. 一些题，需要对贪心算法做调整，例如从后往前贪心
5. 面试时，若用到二分查找，最好说明能用二分查找的条件：有序（升序/降序）、有界（最大值和最小值）、能索引（例如链表就不太好做）

Week 6

1. 动态规划和递归/分治，没有根本上的区别：都是找重复性
2. 非要说动态规划和递归/分治的区别：动态规划只需最存优子结构，中途会淘汰次优解
2. 动态规划一般步骤：拆解成子问题（找重复性）→定义状态数组（状态定义）→DP方程

Week 7

1. Trie树/字典树：减少无效的字符串比较，用于query推荐
2. Trie树，对小写英文来说，最坏的情况，是26叉树
3. 并查集：用于组团、匹配问题，例如两个人是否好友、圈子里有多少个好友圈等
4. 回溯、BFS、DFS可加入剪枝
5. 找两个点的最小步数，可用双向BFS

Week 8

1. 位运算：<<左移，>>右移，|或，&与，~取反，^异或
2. a&b且二者长度不同时，截取最短的
3. 要记住常见的，例如：x&1代表x%2，x>>1代表x//2，x&(x-1)代表清零最低位的1，x&-x代表得到最低位的1(注意区别:x&~x得到0)
4. 布隆过滤器：映射成二进制向量，用于粗略判断元素是否在集合中（只能检查一个元素是否在集合中，而不能像哈希表一样根据key提取value）
5. LRU缓存：key-value形式，超出容量则会删除最远未使用（least recently used最少最近）的元素，通过哈希表指向一个双向链表来实现，修改、查询、更新均为O(1)
6. 选择排序，O(N^2)：每次选最小值放到起始位置
7. 插入排序，O(N^2)：保证左侧是有序的，逐渐将右侧的插进来
8. 冒泡排序，O(N^2)：每次比较相邻元素，若逆序了则交换
9. 快速排序，O(NlogN)，最差O(N^2)：选一个标杆（例如选取首位），小于其的放左边，大于其的放右边；然后对子序列继续快排
10. 归并排序，O(NlogN)：均匀划分为左右；然后对左右子序列继续划分；最后将子序列合并（在合并过程中排序）
11. 堆排序，O(NlogN)：元素依次插入小顶堆；依次取堆顶元素并删除
12. 计数排序、桶排序、基数排序均只能对整数（有限数目）操作

Week 9

1. 高级动态规划：维度更高、状态更复杂

2020.8.31 完