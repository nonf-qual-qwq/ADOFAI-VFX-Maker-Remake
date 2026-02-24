## 这里是AVM的wiki

我是nonf-qual，目前只是一个业余爱好者。

AVM全程ADOFAI VFX Maker，是一个优化ADOFAI特效的程序。

目前是用json结构来编写的

大概写法是：

    {
        "method_1":[
            {
                "key_1" : "value_1",
                "key_2" : "value_2"
            },
            {
                "key_1" : "value_1",
                "key_2" : "value_2"      
            }
        ]
        "method_2":[
            {
                "key_1" : "value_1",
                "key_2" : "value_2"
            }
        ]
    }

**方法有三种:**

MoveTrack:移动轨道

AddDecoration:添加装饰

MoveDecorations:移动装饰

**表达式有三种:**

1.random_[x,y]:表示随机取x~y之间的数值

2.recursion_[x,y,z]:表示在x~y中平均分割z-1份所取出的一组数:一共有z个数（包括x和y,从小到大排列）

3.recursion_d_[x,y,z]:表示在x~y中平均分割z-1份所取出的一组数:一共有z个数（包括x和y,从大到小排列）

**如何查询方法相对应的属性:**

因为有懒b不想写wiki，所以只能你们自己去找对应的。

src/lib/handle/lib.py是一些属性的关键词（也就是某个属性必须填这个里面中的一个）

src/lib/method是相对应的方法
那么怎么看呢？

1.点开你要来看的
2.里面都会有一个result字典，字典所有的键都对应游戏代码里面的关键字
所有的值所相对应的dict的关键字，就是你可以填写的关键词。

比如:

        ro = has.has_num(dict, "ro", 0, num)
        result["rotationOffset"] = ro

ro就是你可以填写的关键词，所对应游戏里面是rotationOffset

特殊的，比如所有的num表示你要生成num个方法


