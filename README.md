# python-target-offer
备战刷题《剑指offer》python的实现

## 排序
### [冒泡排序](https://github.com/jiyali/python-target-offer/blob/master/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F.py)
1、把第一个元素与第二个元素比较，如果第一个比第二个大，则交换他们的位置。接着继续比较第二个与第三个元素，如果第二个比第三个大，则交换他们的位置….
我们对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样一趟比较交换下来之后，排在最右的元素就会是最大的数。
除去最右的元素，我们对剩余的元素做同样的工作，如此重复下去，直到排序完成。
性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序

### [选择排序](https://github.com/jiyali/python-target-offer/blob/master/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F.py)
首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置(如果第一个元素就是最小元素那么它就和自己交换)。其次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。这种方法我们称之为选择排序。
性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、非稳定排序  4、原地排序

### [插入排序](https://github.com/jiyali/python-target-offer/blob/master/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.py)
过程简单描述：
1、从数组第2个元素开始抽取元素。
2、把它与左边第一个元素比较，如果左边第一个元素比它大，则继续与左边第二个元素比较下去，直到遇到不比它大的元素，然后插到这个元素的右边。
3、继续选取第3，4，….n个元素,重复步骤 2 ，选择适当的位置插入。
性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序

### [希尔排序](https://github.com/jiyali/python-target-offer/blob/master/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F.py)
希尔排序可以说是插入排序的一种变种。无论是插入排序还是冒泡排序，如果数组的最大值刚好是在第一位，要将它挪到正确的位置就需要 n - 1 次移动。也就是说，原数组的一个元素如果距离它正确的位置很远的话，则需要与相邻元素交换很多次才能到达正确的位置，这样是相对比较花时间了。
希尔排序就是为了加快速度简单地改进了插入排序，交换不相邻的元素以对数组的局部进行排序。
希尔排序的思想是采用插入排序的方法，先让数组中任意间隔为 h 的元素有序，刚开始 h 的大小可以是 h = n / 2,接着让 h = n / 4，让 h 一直缩小，当 h = 1 时，也就是此时数组中任意间隔为1的元素有序，此时的数组就是有序的了。
性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序

### [归并排序](https://github.com/jiyali/python-target-offer/blob/master/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F.py)
将一个大的无序数组有序，我们可以把大的数组分成两个，然后对这两个数组分别进行排序，之后在把这两个数组合并成一个有序的数组。由于两个小的数组都是有序的，所以在合并的时候是很快的。
通过递归的方式将大的数组一直分割，直到数组的大小为 1，此时只有一个元素，那么该数组就是有序的了，之后再把两个数组大小为1的合并成一个大小为2的，再把两个大小为2的合并成4的 ….. 直到全部小的数组合并起来。
性质：1、时间复杂度：O(nlogn)  2、空间复杂度：O(n)  3、稳定排序  4、非原地排序


### [快速排序](https://github.com/jiyali/python-target-offer/blob/master/11_01%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F.py)
我们从数组中选择一个元素，我们把这个元素称之为中轴元素吧，然后把数组中所有小于中轴元素的元素放在其左边，所有大于或等于中轴元素的元素放在其右边，显然，此时中轴元素所处的位置的是有序的。也就是说，我们无需再移动中轴元素的位置。
从中轴元素那里开始把大的数组切割成两个小的数组(两个数组都不包含中轴元素)，接着我们通过递归的方式，让中轴元素左边的数组和右边的数组也重复同样的操作，直到数组的大小为1，此时每个元素都处于有序的位置。
性质：1、时间复杂度：O(nlogn)  2、空间复杂度：O(logn)  3、非稳定排序  4、原地排序

### [堆排序]()
堆的特点就是堆顶的元素是一个最值，大顶堆的堆顶是最大值，小顶堆则是最小值。
堆排序就是把堆顶的元素与最后一个元素交换，交换之后破坏了堆的特性，我们再把堆中剩余的元素再次构成一个大顶堆，然后再把堆顶元素与最后第二个元素交换….如此往复下去，等到剩余的元素只有一个的时候，此时的数组就是有序的了。

### 链表
* [leetcode2 两数相加](https://github.com/jiyali/python-target-offer/blob/master/leetcode002_%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0.py)
* [leetcode19 删除链表的倒数第N个节点](https://github.com/jiyali/python-target-offer/blob/master/leetcode019_%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.py)
* [leetcode21 合并两个有序链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode021_%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8.py)
* [leetcode23 合并K个排序链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode023_%E5%90%88%E5%B9%B6k%E4%B8%AA%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8.py)
* [leetcode24 两两交换链表中的节点](https://github.com/jiyali/python-target-offer/blob/master/leetcode024_%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.py)
* [leetcode25 k个一组翻转链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode025_k%E4%B8%AA%E4%B8%80%E7%BB%84%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.py)
* [leetcode61 旋转链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode061_%E6%97%8B%E8%BD%AC%E9%93%BE%E8%A1%A8.py)
* [leetcode82 删除排序链表中的重复元素II](https://github.com/jiyali/python-target-offer/blob/master/leetcode082_%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0II.py)
* [leetcode83 删除排序链表中的重复元素](https://github.com/jiyali/python-target-offer/blob/master/leetcode083_%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0.py)
* [leetcode86 分隔链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode086_%E5%88%86%E9%9A%94%E9%93%BE%E8%A1%A8.py)
* [leetcode206 反转链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode206_%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)
* [leetcode92 反转链表II](https://github.com/jiyali/python-target-offer/blob/master/leetcode092_%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8II.py)
* [leetcode109 有序链表转换二叉搜索树](https://github.com/jiyali/python-target-offer/blob/master/leetcode109_%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8%E8%BD%AC%E6%8D%A2%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.py)
* [leetcode138 复制带随机指针的链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode138_%E5%A4%8D%E5%88%B6%E5%B8%A6%E9%9A%8F%E6%9C%BA%E6%8C%87%E9%92%88%E7%9A%84%E9%93%BE%E8%A1%A8.py)
* [leetcode141 环形链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode141_%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8.py)
* [leetcode142 环形链表II](https://github.com/jiyali/python-target-offer/blob/master/leetcode142_%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.py)
* [leetcode143 重排链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode143_%E9%87%8D%E6%8E%92%E9%93%BE%E8%A1%A8.py)
* [leetcode147 对链表进行插入排序](https://github.com/jiyali/python-target-offer/blob/master/leetcode147_%E5%AF%B9%E9%93%BE%E8%A1%A8%E8%BF%9B%E8%A1%8C%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F.py)
* [leetcode148 排序链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode148_%E6%8E%92%E5%BA%8F%E9%93%BE%E8%A1%A8.py)
* [leetcode160 相交链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode160_%E7%9B%B8%E4%BA%A4%E9%93%BE%E8%A1%A8.py)
* [leetcode203 移除链表元素](https://github.com/jiyali/python-target-offer/blob/master/leetcode203_%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.py)
* [leetcode206 反转链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode206_%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)
* [leetcode234 回文链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode234_%E5%9B%9E%E6%96%87%E9%93%BE%E8%A1%A8.py)
* [leetcode237 删除链表中的节点](https://github.com/jiyali/python-target-offer/blob/master/leetcode237_%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.py)
* [leetcode318 奇偶链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode328_%E5%A5%87%E5%81%B6%E9%93%BE%E8%A1%A8.py)
* [leetcode445 两数相加II](https://github.com/jiyali/python-target-offer/blob/master/leetcode445_%E4%B8%A4%E6%95%B0%E7%9B%B8%E5%8A%A0II.py)
* [leetcode430 扁平化多级双向链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode430_%E6%89%81%E5%B9%B3%E5%8C%96%E5%A4%9A%E7%BA%A7%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.py)
* [leetcode725 分隔链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode725_%E5%88%86%E9%9A%94%E9%93%BE%E8%A1%A8.py)
* [leetcode876 链表的中间结点](https://github.com/jiyali/python-target-offer/blob/master/leetcode876_%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%97%B4%E7%BB%93%E7%82%B9.py)
* [leetcode 1290 二进制链表转整数](https://github.com/jiyali/python-target-offer/blob/master/leetcode1290_%E4%BA%8C%E8%BF%9B%E5%88%B6%E9%93%BE%E8%A1%A8%E8%BD%AC%E6%95%B4%E6%95%B0.py)
* [剑指offer06_01 逆序打印链表](https://github.com/jiyali/python-target-offer/blob/master/06_01%E9%80%86%E5%BA%8F%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py)
* [剑指offer06_02 逆序打印链表](https://github.com/jiyali/python-target-offer/blob/master/06_02%E9%80%86%E5%BA%8F%E6%89%93%E5%8D%B0%E9%93%BE%E8%A1%A8.py)
* [剑指offer18_01 删除链表中的节点](https://github.com/jiyali/python-target-offer/blob/master/18_01%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E8%8A%82%E7%82%B9.py)
* [剑指offer18_02 删除链表中的重复节点](https://github.com/jiyali/python-target-offer/blob/master/18_02%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E8%8A%82%E7%82%B9.py)
* [剑指offer22_01 链表中倒数第k个节点](https://github.com/jiyali/python-target-offer/blob/master/22_01%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%92%E6%95%B0%E7%AC%ACk%E4%B8%AA%E8%8A%82%E7%82%B9.py)
* [剑指offer22_02 求链表中的中间节点](https://github.com/jiyali/python-target-offer/blob/master/22_02%E6%B1%82%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%97%B4%E8%8A%82%E7%82%B9.py)
* [剑指offer23 链表中环的入口节点](https://github.com/jiyali/python-target-offer/blob/master/23_%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%8E%AF%E7%9A%84%E5%85%A5%E5%8F%A3%E8%8A%82%E7%82%B9.py)
* [剑指offer24 反转链表](https://github.com/jiyali/python-target-offer/blob/master/24_%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.py)
* [剑指offer25 合并两个排序的链表](https://github.com/jiyali/python-target-offer/blob/master/25_%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%8E%92%E5%BA%8F%E7%9A%84%E9%93%BE%E8%A1%A8.py)
* [剑指offer35_01 复杂链表的复制](https://github.com/jiyali/python-target-offer/blob/master/35_01%E5%A4%8D%E6%9D%82%E9%93%BE%E8%A1%A8%E7%9A%84%E5%A4%8D%E5%88%B6.py) 
* [真题 找出单向链表中的一个节点，该节点到尾指针的距离为K](https://github.com/jiyali/python-target-offer/blob/master/%E7%9C%9F%E9%A2%98_%E6%89%BE%E5%87%BA%E5%8D%95%E5%90%91%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E4%B8%80%E4%B8%AA%E8%8A%82%E7%82%B9%EF%BC%8C%E8%AF%A5%E8%8A%82%E7%82%B9%E5%88%B0%E5%B0%BE%E6%8C%87%E9%92%88%E7%9A%84%E8%B7%9D%E7%A6%BB%E4%B8%BAk.py)

### 数组
* [leetcode1 两数之和](https://github.com/jiyali/python-target-offer/blob/master/leetcode001_%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.py)
* [leetcode4 寻找两个有序数组的中位数](https://github.com/jiyali/python-target-offer/blob/master/leetcode004_%E5%AF%BB%E6%89%BE%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E4%B8%AD%E4%BD%8D%E6%95%B0.py)
* [leetcode11 盛最多水的容器](https://github.com/jiyali/python-target-offer/blob/master/leetcode011_%E7%9B%9B%E6%9C%80%E5%A4%9A%E6%B0%B4%E7%9A%84%E5%AE%B9%E5%99%A8.py)
* [leetcode15 三数之和](https://github.com/jiyali/python-target-offer/blob/master/leetcode015_%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.py)
* [leetcode16 最接近的三数之和](https://github.com/jiyali/python-target-offer/blob/master/leetcode016_%E6%9C%80%E6%8E%A5%E8%BF%91%E7%9A%84%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.py)
* [leetcode26 删除排序数组中的重复项](https://github.com/jiyali/python-target-offer/blob/master/leetcode026_%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E9%A1%B9.py)
* [leetcode27 移除元素](https://github.com/jiyali/python-target-offer/blob/master/leetcode027_%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.py)
* [leetcode42 接雨水](https://github.com/jiyali/python-target-offer/blob/master/leetcode042_%E6%8E%A5%E9%9B%A8%E6%B0%B4.py)
* [leetcode53 最大子序和](https://github.com/jiyali/python-target-offer/blob/master/leetcode053_%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.py)
* [leetcode62 不同路径](https://github.com/jiyali/python-target-offer/blob/master/leetcode062_%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.py)
* [leetcode63 不同路径II](https://github.com/jiyali/python-target-offer/blob/master/leetcode063_%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.py)
* [leetcode64 最小路径和](https://github.com/jiyali/python-target-offer/blob/master/leetcode064_%E6%9C%80%E5%B0%8F%E8%B7%AF%E5%BE%84%E5%92%8C.py)
* [leetcode75 颜色分类](https://github.com/jiyali/python-target-offer/blob/master/leetcode075_%E9%A2%9C%E8%89%B2%E5%88%86%E7%B1%BB.py)
* [leetcode80 删除排序数组中的重复项II](https://github.com/jiyali/python-target-offer/blob/master/leetcode080_%E5%88%A0%E9%99%A4%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E9%87%8D%E5%A4%8D%E9%A1%B9II.py)
* [leetcode88 合并两个有序数组](https://github.com/jiyali/python-target-offer/blob/master/leetcode088_%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84.py)
* [leetcode105 从前序与中序遍历序列构造二叉树](https://github.com/jiyali/python-target-offer/blob/master/leetcode105_%E4%BB%8E%E5%89%8D%E5%BA%8F%E4%B8%8E%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.py)
* [leetcode126 单词接龙II](https://github.com/jiyali/python-target-offer/blob/master/leetcode126_%E5%8D%95%E8%AF%8D%E6%8E%A5%E9%BE%99II.py)
* [leetcode209 长度最小的子数组](https://github.com/jiyali/python-target-offer/blob/master/leetcode209_%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.py)
* [leetcode219 存在重复元素II](https://github.com/jiyali/python-target-offer/blob/master/leetcode219_%E5%AD%98%E5%9C%A8%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0II.py)
* [leetcode283 移动零](https://github.com/jiyali/python-target-offer/blob/master/leetcode283_%E7%A7%BB%E5%8A%A8%E9%9B%B6.py)
* [leetcode695 岛屿的最大面积](https://github.com/jiyali/python-target-offer/blob/master/leetcode695_%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.py)
* [leetcode1013 将数组分成和相等的三个部分](https://github.com/jiyali/python-target-offer/blob/master/leetcode1013_%E5%B0%86%E6%95%B0%E7%BB%84%E5%88%86%E4%B8%BA%E5%92%8C%E7%9B%B8%E7%AD%89%E7%9A%84%E4%B8%89%E4%B8%AA%E9%83%A8%E5%88%86.py)


### 树
* [leetcode94 二叉树的中序遍历](https://github.com/jiyali/python-target-offer/blob/master/leetcode094_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86.py)
* [leetcode98 验证二叉搜索树](https://github.com/jiyali/python-target-offer/blob/master/leetcode095_%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.py)
* [leetcode102 二叉树的层次遍历](https://github.com/jiyali/python-target-offer/blob/master/leetcode102_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86.py)
* [leetcode103 二叉树的锯齿形遍历](https://github.com/jiyali/python-target-offer/blob/master/leetcode103_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%94%AF%E9%BD%BF%E5%BD%A2%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86.py)
* [leetcode104 二叉树的最大深度](https://github.com/jiyali/python-target-offer/blob/master/leetcode104_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.py)
* [leetcode105 从前序与中序遍历序列构造二叉树](https://github.com/jiyali/python-target-offer/blob/master/leetcode105_%E4%BB%8E%E5%89%8D%E5%BA%8F%E4%B8%8E%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.py)
* [leetcode107 二叉树的层次遍历II](https://github.com/jiyali/python-target-offer/blob/master/leetcode107_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E6%AC%A1%E9%81%8D%E5%8E%86%20II.py)
* [leetcode144 二叉树的前序遍历](https://github.com/jiyali/python-target-offer/blob/master/leetcode144_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.py)
* [leetcode145 二叉树的后序遍历](https://github.com/jiyali/python-target-offer/blob/master/leetcode145_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86.py)
* [leetcode199 二叉树的右视图](https://github.com/jiyali/python-target-offer/blob/master/leetcode199_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%8F%B3%E8%A7%86%E5%9B%BE.py)
* [leetcode235 二叉搜索树的最近公共祖先](https://github.com/jiyali/python-target-offer/blob/master/leetcode235_%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)
* [leetcode236 二叉树的最近公共祖先](https://github.com/jiyali/python-target-offer/blob/master/leetcode236_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.py)


### 动态规划
* [leetcode5 最长回文子串](https://github.com/jiyali/python-target-offer/blob/master/leetcode005_%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.py)
* [leetcode53 最大子序和](https://github.com/jiyali/python-target-offer/blob/master/leetcode053_%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.py)
* [leetcode62 不同路径](https://github.com/jiyali/python-target-offer/blob/master/leetcode062_%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.py)
* [leetcode63 不同路径II](https://github.com/jiyali/python-target-offer/blob/master/leetcode063_%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.py)
* [leetcode64 最小路径和](https://github.com/jiyali/python-target-offer/blob/master/leetcode064_%E6%9C%80%E5%B0%8F%E8%B7%AF%E5%BE%84%E5%92%8C.py)
* [leetcode70 爬楼梯](https://github.com/jiyali/python-target-offer/blob/master/leetcode070_%E7%88%AC%E6%A5%BC%E6%A2%AF.py)
* [leetcode91 解码方式](https://github.com/jiyali/python-target-offer/blob/master/leetcode091_%E8%A7%A3%E7%A0%81%E6%96%B9%E5%BC%8F.py)
* [leetcode264 丑数II](https://github.com/jiyali/python-target-offer/blob/master/leetcode264_%E4%B8%91%E6%95%B0II.py)
* [leetcode279 完全平方数](https://github.com/jiyali/python-target-offer/blob/master/leetcode279_%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.py)


### DFS
* [leetcode98 验证二叉搜索树](https://github.com/jiyali/python-target-offer/blob/master/leetcode098_%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.py)
* [leetcode100 相同的树](https://github.com/jiyali/python-target-offer/blob/master/leetcode100_%E7%9B%B8%E5%90%8C%E7%9A%84%E6%A0%91.py)
* [leetcode101 对称二叉树](https://github.com/jiyali/python-target-offer/blob/master/leetcode101_%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.py)
* [leetcode104 二叉树的最大深度](https://github.com/jiyali/python-target-offer/blob/master/leetcode104_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.py)
* [leetcode105 从前序与中序遍历序列构造二叉树](https://github.com/jiyali/python-target-offer/blob/master/leetcode105_%E4%BB%8E%E5%89%8D%E5%BA%8F%E4%B8%8E%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.py)
* [leetcode109 有序链表转换二叉搜索树](https://github.com/jiyali/python-target-offer/blob/master/leetcode109_%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8%E8%BD%AC%E6%8D%A2%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.py)
* [leetcode110 平衡二叉树](https://github.com/jiyali/python-target-offer/blob/master/leetcode110_%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.py)
* [leetcode111 二叉树的最小深度](https://github.com/jiyali/python-target-offer/blob/master/leetcode111_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.py)
* [leetcode112 路径总和](https://github.com/jiyali/python-target-offer/blob/master/leetcode112_%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.py)
* [leetcode113 路径总和II](https://github.com/jiyali/python-target-offer/blob/master/leetcode113_%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8CII.py)
* [leetcode129 求根到叶子节点数字之和](https://github.com/jiyali/python-target-offer/blob/master/leetcode129_%E6%B1%82%E6%A0%B9%E5%88%B0%E5%8F%B6%E5%AD%90%E8%8A%82%E7%82%B9%E6%95%B0%E5%AD%97%E4%B9%8B%E5%92%8C.py)
* [leetcode199 二叉树的右视图](https://github.com/jiyali/python-target-offer/blob/master/leetcode199_%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%8F%B3%E8%A7%86%E5%9B%BE.py)
* [leetcode257 二叉树的所有路径](https://github.com/jiyali/python-target-offer/blob/master/leetcode257%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.py)
* [leetcode695 岛屿的最大面积](https://github.com/jiyali/python-target-offer/blob/master/leetcode695_%E5%B2%9B%E5%B1%BF%E7%9A%84%E6%9C%80%E5%A4%A7%E9%9D%A2%E7%A7%AF.py)
* [leetcode430 扁平化多级双向链表](https://github.com/jiyali/python-target-offer/blob/master/leetcode430_%E6%89%81%E5%B9%B3%E5%8C%96%E5%A4%9A%E7%BA%A7%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8.py)

### 动态规划
* [leetcode5 最长回文子串](https://github.com/jiyali/python-target-offer/blob/master/leetcode005_%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.py)
* [leetcode53 最大子序和](https://github.com/jiyali/python-target-offer/blob/master/leetcode053_%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.py)
* [leetcode62 不同路径](https://github.com/jiyali/python-target-offer/blob/master/leetcode062_%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.py)
* [leetcode63 不同路径II](https://github.com/jiyali/python-target-offer/blob/master/leetcode063_%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.py)
* [leetcode64 最小路径和](https://github.com/jiyali/python-target-offer/blob/master/leetcode064_%E6%9C%80%E5%B0%8F%E8%B7%AF%E5%BE%84%E5%92%8C.py)
* [leetcode70 爬楼梯](https://github.com/jiyali/python-target-offer/blob/master/leetcode070_%E7%88%AC%E6%A5%BC%E6%A2%AF.py)
* [leetcode91 解码方法](https://github.com/jiyali/python-target-offer/blob/master/leetcode091_%E8%A7%A3%E7%A0%81%E6%96%B9%E5%BC%8F.py)
* [leetcode264 丑数II](https://github.com/jiyali/python-target-offer/blob/master/leetcode264_%E4%B8%91%E6%95%B0II.py)
* [leetcode279 完全平方数](https://github.com/jiyali/python-target-offer/blob/master/leetcode279_%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.py)
* [leetcode322 零钱兑换](https://github.com/jiyali/python-target-offer/blob/master/leetcode322_%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.py)
* [leetcode1143 最长公共子序列](https://github.com/jiyali/python-target-offer/blob/master/leetcode1143_%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.py)

# 回溯
* [leetcode17 电话号码的字母组合](https://github.com/jiyali/python-target-offer/blob/master/leetcode017_%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.py)
* [leetcode22 括号生成](https://github.com/jiyali/python-target-offer/blob/master/leetcode022_%E6%8B%AC%E5%8F%B7%E7%94%9F%E6%88%90.py)
* [leetcode39 组合总和](https://github.com/jiyali/python-target-offer/blob/master/leetcode039_%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.py)
* [leetcode46 全排列](https://github.com/jiyali/python-target-offer/blob/master/leetcode046_%E5%85%A8%E6%8E%92%E5%88%97.py)
* [leetcode47 全排列II](https://github.com/jiyali/python-target-offer/blob/master/leetcode047_%E5%85%A8%E6%8E%92%E5%88%97II.py)
* [leetcode49 组合总和II](https://github.com/jiyali/python-target-offer/blob/master/leetcode049_%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.py)
* [leetcode60 第k个排列](https://github.com/jiyali/python-target-offer/blob/master/leetcode060_%E7%AC%ACk%E4%B8%AA%E6%8E%92%E5%88%97.py)
* [leetcode77 组合](https://github.com/jiyali/python-target-offer/blob/master/leetcode077_%E7%BB%84%E5%90%88.py)
* [leetcode78 子集](https://github.com/jiyali/python-target-offer/blob/master/leetcode078_%E5%AD%90%E9%9B%86.py)
* [leetcode90 子集II](https://github.com/jiyali/python-target-offer/blob/master/leetcode090_%E5%AD%90%E9%9B%86II.py)
* [leetcode784 字母大小写全排列](https://github.com/jiyali/python-target-offer/blob/master/leetcode784_%E5%AD%97%E6%AF%8D%E5%A4%A7%E5%B0%8F%E5%85%A8%E6%8E%92%E5%88%97.py)
