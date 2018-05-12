 # -*- coding: utf-8 -*-  
import numpy as np 

def main():
     #line
     import matplotlib.pyplot as plt     
     x=np.linspace(-np.pi, np.pi, 256, endpoint=True)
     c,s=np.cos(x), np.sin(x)
     plt.figure(1)
     plt.plot(x,c,color="blue", linewidth=1.0,linestyle="-",label="COS", alpha=0.5)
     plt.plot(x,s, "r*", label="SIN")
     plt.title("COS & SIN")
     ax=plt.gca()
     ax.spines["right"].set_color("none")
     ax.spines["top"].set_color("none")
     ax.spines["left"].set_position(("data",0))
     ax.spines["bottom"].set_position(("data",0))
     ax.xaxis.set_ticks_position("bottom")
     ax.yaxis.set_ticks_position("left")
     plt.xticks(np.linspace(-np.pi,np.pi,5,endpoint=True))  #设置x轴的标注位于bottom轴
     plt.yticks(np.linspace(-1,1,5,endpoint=True))
     for label in ax.get_xticklabels()+ax.get_yticklabels():
         #改变label的大小
         label.set_fontsize(16)
         #设置label的小方块及其背景
         label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))
     plt.legend(loc="upper left")
     plt.grid()
     # 范围
     # plt.axis([-1, 1, -0.5, 1])
     #当x绝对值小于0.5，为真记为1，此范围内从1开始到曲线cosx填充，其余为0开始到曲线cosx填充，c>0.5确定横轴范围x,保证c=cosx>0.5
     plt.fill_between(x, np.abs(x)<0.5,c,c>0.5,color="green",alpha=0.25)
     t=1
     plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")
     plt.show()
     
if __name__=="__main__":
    main()