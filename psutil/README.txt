这些进程已经死亡，但没有释放系统资源，包括内存和一些一些系统表等，如果这样的进程很多，会引发系统问题。用ps -el看出的进程状态如果是Z，就是僵尸进程。 
　　ps -ef|grep defunc可以找出僵尸进程. 
　　有些ZOMBIE进程时用kill -9也不能杀死，而且消耗了很多系统资源不能释放，如果系统在shutdown时发出信息:some process wouldn’t die. 这就意味这有些进程不能被reboot发出的kill –9杀掉，这些很可能就是僵尸进程。 

　　可以用ps 的 – l 选项,得到更详细的进程信息. 
　　F(Flag)：一系列数字的和，表示进程的当前状态。这些数字的含义为： 
　　00：若单独显示，表示此进程已被终止。 
　　01：进程是核心进程的一部分，常驻于系统主存。如：　　　 sched、 vhand 、bdflush 等。 
　　02：Parent is tracing process. 
　　04 ：Tracing parent's signal has stopped the process; the parent　is waiting ( ptrace(S)). 
　　10：进程在优先级低于或等于25时，进入休眠状态，而且不能用信号唤醒，例如在等待一个inode被创建时　　　 
　　20：进程被装入主存（primary memory） 
　　40：进程被锁在主存，在事务完成前不能被置换　　　e 
　　S(state of the process ) 
　　O：进程正在处理器运行　 
　　S：休眠状态（sleeping） 
　　R：等待运行（runable）　　　 
　　I：空闲状态（idle） 
　　Z：僵尸状态（zombie）　　　 
　　T：跟踪状态（Traced） 
　　B：进程正在等待更多的内存页 
　　C(cpu usage)：cpu利用率的估算值 

　　清除ZOMBIE（僵尸）进程可以使用如下方法： 
　　1> kill –18 PPID （PPID是其父进程） 
　　这个信号是告诉父进程，该子进程已经死亡了，请收回分配给他的资源。 
　　2>如果不行则看能否终止其父进程（如果其父进程不需要的话）。先看其父进程又无其他子进程，如果有，可能需要先kill其他子进程，也就是兄弟进程。方法是： 
　　kill –15 PID1 PID2(PID1,PID2是僵尸进程的父进程的其它子进程)。 
　　然后再kill父进程：kill –15 PPID 

　　这样僵尸进程就可能被完全杀掉了。
