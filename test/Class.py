# -*- coding: utf-8 -*-
import numpy as np
#import seaborn as sns
#import scipy.stats as sp
from scipy.fftpack import fft
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from scipy import stats

# =============================================================================
# functionクラス
# =============================================================================
class Function:
    def __init__(self, data):
        self.data = data
    
    #標準化(平均0、分散1)
    """scipyの関数を使用"""
    def Standardization(self,x):
        return sp.stats.zscore(x)

    #平均値
    def Average(self,x):
        return np.average(x)
    
    #分散
    def Variance(self,x):
        return np.var(x)

    #標準偏差
    def Std(self,x):
        return np.std(x)
    
    #検定統計量
    def T(self,x):
        av = Function.Average(self,x)
        std = Function.Std(self,x)
        return (x-av)/std

# =============================================================================
# calculationクラス
# =============================================================================
class Clustering:
    def __init__(self, data):
        self.data = data
        self.Time,self.X,self.Y,self.X_obj,self.Y_obj,self.Vx,self.Vy,self.V_obj,self.blackout,self.Ax,self.Ay,self.steer,self.throttle,self.thr_eng,self.ELSE = np.hsplit(self.data,[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    
    #微分計算
    def diff4(x, h):
        res = -x[4:] + 8*x[3:-1] - 8*x[1:-3] + x[:-4]
        return res/(12*h)
    
    def Cal_para_20201228(self):
        
        #形式変更
        time = self.Time.reshape([self.Time.shape[0],1])
        time = time - 60
        self.blackout[0] = 1
        blackout = np.append(self.blackout,1)

        #Clustering.FFT(self,self.Ax[6000:9000])
        """先行車との距離計算"""
        IVD_Y = self.Y - self.Y_obj
        IVD_X = self.X_obj - self.X
        IVD = np.sqrt(np.square(IVD_X) + np.square(IVD_Y))
        
        """Carsimのバグ消去"""
        for i in range(IVD.shape[0]):
            if IVD[i] > 200:
                IVD_X[i],IVD_Y[i],IVD[i] = IVD_X[i-1],IVD_Y[i-1],IVD[i-1]
        IVD_Y = IVD_Y + 0.25
        
        time_to_collision = IVD/self.Vx
        Jerk_x = Clustering.diff4(self.Ax,0.01)
        Jerk_xp = np.power(Jerk_x,2)
        Jerk_y = Clustering.diff4(self.Ay,0.01)
        Jerk_yp = np.power(Jerk_y,2)
        blackout = self.blackout.reshape([self.blackout.shape[0]])
        #窓枠の変更
        #0.1～5.0秒の窓枠
        i = 30
        I = 10*(i+1)
        A = np.full(I,1/I)
        rateblackout = np.convolve(blackout,A,mode='same')
        rateblackout = rateblackout.reshape([self.blackout.shape[0],1])

        #######################################
        #先行車距離
        #######################################
        #最小，最大，平均，標準偏差
        TTC = [time_to_collision[6000:9000],time_to_collision[9000:12000],time_to_collision[12000:15000],time_to_collision[15000:18000],time_to_collision[18000:21000],time_to_collision[21000:24000],time_to_collision[24000:27000],time_to_collision[27000:30000],time_to_collision[30000:33000],time_to_collision[33000:36000],time_to_collision[36000:39000],time_to_collision[39000:42000]]
        
        #######################################
        #縦躍度
        #######################################
        J_x = [Jerk_xp[6000:9000],Jerk_xp[9000:12000],Jerk_xp[12000:15000],Jerk_xp[15000:18000],Jerk_xp[18000:21000],Jerk_xp[21000:24000],Jerk_xp[24000:27000],Jerk_xp[27000:30000],Jerk_xp[30000:33000],Jerk_xp[33000:36000],Jerk_xp[36000:39000],Jerk_xp[39000:42000]]
        J_y = [Jerk_yp[6000:9000],Jerk_yp[9000:12000],Jerk_yp[12000:15000],Jerk_yp[15000:18000],Jerk_yp[18000:21000],Jerk_yp[21000:24000],Jerk_yp[24000:27000],Jerk_yp[27000:30000],Jerk_yp[30000:33000],Jerk_yp[33000:36000],Jerk_yp[36000:39000],Jerk_yp[39000:42000]]
        #######################################
        #縦位置
        #######################################
        LP = [IVD_Y[6000:9000],IVD_Y[9000:12000],IVD_Y[12000:15000],IVD_Y[15000:18000],IVD_Y[18000:21000],IVD_Y[21000:24000],IVD_Y[24000:27000],IVD_Y[27000:30000],IVD_Y[30000:33000],IVD_Y[33000:36000],IVD_Y[36000:39000],IVD_Y[39000:42000]]

        #######################################
        #視覚課題パフォーマンス
        #######################################
        RB = [rateblackout[6000:9000],rateblackout[9000:12000],rateblackout[12000:15000],rateblackout[15000:18000],rateblackout[18000:21000],rateblackout[21000:24000],rateblackout[24000:27000],rateblackout[27000:30000],rateblackout[30000:33000],rateblackout[33000:36000],rateblackout[36000:39000],rateblackout[39000:42000]]

        out = [TTC,J_x,LP,J_y]#,RB]
        return out

 
    def Cal_para(self):
        
        #形式変更
        time = self.Time.reshape([self.Time.shape[0],1])
        time = time - 60
        self.blackout[0] = 1
        blackout = np.append(self.blackout,1)
        #差分計算（立ち上がりが1，立下りが-1）
        #print(self.blackout.shape)
        flag_blackout = np.diff(blackout,axis = 0)
        #末尾に0を追加
        #flag_blackout = np.append(flag_blackout,0)
        #print(flag_blackout.shape)
        
        #わき見頻度
        #print(np.sum(flag_blackout == -1))
        #わき見時間（-1～1の時間？？）
        time_flag_blackout_p1 = time[flag_blackout == 1]
        time_flag_blackout_m1 = time[flag_blackout == -1]
        time_flag_blackout = time_flag_blackout_p1 - time_flag_blackout_m1
        
        #Clustering.FFT(self,self.Ax[6000:9000])
        """先行車との距離計算"""
        rateblackout = self.Y - self.Y_obj
        IVD_X = self.X_obj - self.X
        IVD = np.sqrt(np.square(IVD_X) + np.square(IVD_Y))
        
        """Carsimのバグ消去"""
        for i in range(IVD.shape[0]):
            if IVD[i] > 200:
                IVD_X[i],IVD_Y[i],IVD[i] = IVD_X[i-1],IVD_Y[i-1],IVD[i-1]
        IVD_Y = IVD_Y + 0.25
        
        #急加速，急減速頻度の計算
        ax_pp = np.where(self.Ax > 0, 1, 0)
        ax_mm = np.where(self.Ax < 0, 1, 0)
        flag_ax_pp = np.diff(ax_pp,axis = 0)
        flag_ax_mm = np.diff(ax_mm,axis = 0)
        #y加速度最大
        Ay = abs(self.Ay)
        Steer = abs(self.steer)
        V_Steer = 100 * np.diff(Steer, n=1 ,axis=0)

        #######################################
        #先行車距離
        #######################################
        #最小，最大，平均，標準偏差
        IVD_min = [np.min(IVD[6000:9000]),np.min(IVD[9000:12000]),np.min(IVD[12000:15000]),np.min(IVD[15000:18000]),np.min(IVD[18000:21000]),np.min(IVD[21000:24000]),np.min(IVD[24000:27000]),np.min(IVD[27000:30000]),np.min(IVD[30000:33000]),np.min(IVD[33000:36000]),np.min(IVD[36000:39000]),np.min(IVD[39000:42000])]
        IVD_max = [np.max(IVD[6000:9000]),np.max(IVD[9000:12000]),np.max(IVD[12000:15000]),np.max(IVD[15000:18000]),np.max(IVD[18000:21000]),np.max(IVD[21000:24000]),np.max(IVD[24000:27000]),np.max(IVD[27000:30000]),np.max(IVD[30000:33000]),np.max(IVD[33000:36000]),np.max(IVD[36000:39000]),np.max(IVD[39000:42000])]
        IVD_av = [np.average(IVD[6000:9000]),np.average(IVD[9000:12000]),np.average(IVD[12000:15000]),np.average(IVD[15000:18000]),np.average(IVD[18000:21000]),np.average(IVD[21000:24000]),np.average(IVD[24000:27000]),np.average(IVD[27000:30000]),np.average(IVD[30000:33000]),np.average(IVD[33000:36000]),np.average(IVD[36000:39000]),np.average(IVD[39000:42000])]
        IVD_sd = [np.std(IVD[6000:9000]),np.std(IVD[9000:12000]),np.std(IVD[12000:15000]),np.std(IVD[15000:18000]),np.std(IVD[18000:21000]),np.std(IVD[21000:24000]),np.std(IVD[24000:27000]),np.std(IVD[27000:30000]),np.std(IVD[30000:33000]),np.std(IVD[33000:36000]),np.std(IVD[36000:39000]),np.std(IVD[39000:42000])]

        #######################################
        #縦加速度
        #######################################
        #最小，最大，平均，標準偏差
        Ax_min = [np.min(self.Ax[6000:9000]),np.min(self.Ax[9000:12000]),np.min(self.Ax[12000:15000]),np.min(self.Ax[15000:18000]),np.min(self.Ax[18000:21000]),np.min(self.Ax[21000:24000]),np.min(self.Ax[24000:27000]),np.min(self.Ax[27000:30000]),np.min(self.Ax[30000:33000]),np.min(self.Ax[33000:36000]),np.min(self.Ax[36000:39000]),np.min(self.Ax[39000:42000])]
        Ax_max = [np.max(self.Ax[6000:9000]),np.max(self.Ax[9000:12000]),np.max(self.Ax[12000:15000]),np.max(self.Ax[15000:18000]),np.max(self.Ax[18000:21000]),np.max(self.Ax[21000:24000]),np.max(self.Ax[24000:27000]),np.max(self.Ax[27000:30000]),np.max(self.Ax[30000:33000]),np.max(self.Ax[33000:36000]),np.max(self.Ax[36000:39000]),np.max(self.Ax[39000:42000])]
        Ax_av = [np.average(self.Ax[6000:9000]),np.average(self.Ax[9000:12000]),np.average(self.Ax[12000:15000]),np.average(self.Ax[15000:18000]),np.average(self.Ax[18000:21000]),np.average(self.Ax[21000:24000]),np.average(self.Ax[24000:27000]),np.average(self.Ax[27000:30000]),np.average(self.Ax[30000:33000]),np.average(self.Ax[33000:36000]),np.average(self.Ax[36000:39000]),np.average(self.Ax[39000:42000])]
        Ax_sd = [np.std(self.Ax[6000:9000]),np.std(self.Ax[9000:12000]),np.std(self.Ax[12000:15000]),np.std(self.Ax[15000:18000]),np.std(self.Ax[18000:21000]),np.std(self.Ax[21000:24000]),np.std(self.Ax[24000:27000]),np.std(self.Ax[27000:30000]),np.std(self.Ax[30000:33000]),np.std(self.Ax[33000:36000]),np.std(self.Ax[36000:39000]),np.std(self.Ax[39000:42000])]
        
        #頻度
        Ax_freq_acc = [np.sum(flag_ax_pp[6000:9000] == -1),np.sum(flag_ax_pp[9000:12000] == -1),np.sum(flag_ax_pp[12000:15000] == -1),np.sum(flag_ax_pp[15000:18000] == -1),np.sum(flag_ax_pp[18000:21000] == -1),np.sum(flag_ax_pp[21000:24000] == -1),np.sum(flag_ax_pp[24000:27000] == -1),np.sum(flag_ax_pp[27000:30000] == -1),np.sum(flag_ax_pp[30000:33000] == -1),np.sum(flag_ax_pp[33000:36000] == -1),np.sum(flag_ax_pp[36000:39000] == -1),np.sum(flag_ax_pp[39000:42000] == -1)]
        Ax_freq_dec = [np.sum(flag_ax_mm[6000:9000] == -1),np.sum(flag_ax_mm[9000:12000] == -1),np.sum(flag_ax_mm[12000:15000] == -1),np.sum(flag_ax_mm[15000:18000] == -1),np.sum(flag_ax_mm[18000:21000] == -1),np.sum(flag_ax_mm[21000:24000] == -1),np.sum(flag_ax_mm[24000:27000] == -1),np.sum(flag_ax_mm[27000:30000] == -1),np.sum(flag_ax_mm[30000:33000] == -1),np.sum(flag_ax_mm[33000:36000] == -1),np.sum(flag_ax_mm[36000:39000] == -1),np.sum(flag_ax_mm[39000:42000] == -1)]
        
        #######################################
        #ステアリング
        #######################################
        #最小，最大，平均，標準偏差
        Steer_min = [np.min(self.steer[6000:9000]),np.min(self.steer[9000:12000]),np.min(self.steer[12000:15000]),np.min(self.steer[15000:18000]),np.min(self.steer[18000:21000]),np.min(self.steer[21000:24000]),np.min(self.steer[24000:27000]),np.min(self.steer[27000:30000]),np.min(self.steer[30000:33000]),np.min(self.steer[33000:36000]),np.min(self.steer[36000:39000]),np.min(self.steer[39000:42000])]
        Steer_max = [np.max(self.steer[6000:9000]),np.max(self.steer[9000:12000]),np.max(self.steer[12000:15000]),np.max(self.steer[15000:18000]),np.max(self.steer[18000:21000]),np.max(self.steer[21000:24000]),np.max(self.steer[24000:27000]),np.max(self.steer[27000:30000]),np.max(self.steer[30000:33000]),np.max(self.steer[33000:36000]),np.max(self.steer[36000:39000]),np.max(self.steer[39000:42000])]
        Steer_av = [np.average(self.steer[6000:9000]),np.average(self.steer[9000:12000]),np.average(self.steer[12000:15000]),np.average(self.steer[15000:18000]),np.average(self.steer[18000:21000]),np.average(self.steer[21000:24000]),np.average(self.steer[24000:27000]),np.average(self.steer[27000:30000]),np.average(self.steer[30000:33000]),np.average(self.steer[33000:36000]),np.average(self.steer[36000:39000]),np.average(self.steer[39000:42000])]
        Steer_sd = [np.std(self.steer[6000:9000]),np.std(self.steer[9000:12000]),np.std(self.steer[12000:15000]),np.std(self.steer[15000:18000]),np.std(self.steer[18000:21000]),np.std(self.steer[21000:24000]),np.std(self.steer[24000:27000]),np.std(self.steer[27000:30000]),np.std(self.steer[30000:33000]),np.std(self.steer[33000:36000]),np.std(self.steer[36000:39000]),np.std(self.steer[39000:42000])]
        
        #周波数
        Steer_FFT_L = [Clustering.FFT_L(self,self.Ax[6000:9000]),Clustering.FFT_L(self,self.Ax[9000:12000]),Clustering.FFT_L(self,self.Ax[12000:15000]),Clustering.FFT_L(self,self.Ax[15000:18000]),Clustering.FFT_L(self,self.Ax[18000:21000]),Clustering.FFT_L(self,self.Ax[21000:24000]),Clustering.FFT_L(self,self.Ax[24000:27000]),Clustering.FFT_L(self,self.Ax[27000:30000]),Clustering.FFT_L(self,self.Ax[30000:33000]),Clustering.FFT_L(self,self.Ax[33000:36000]),Clustering.FFT_L(self,self.Ax[36000:39000]),Clustering.FFT_L(self,self.Ax[39000:42000])]
        Steer_FFT_H = [Clustering.FFT_H(self,self.Ax[6000:9000]),Clustering.FFT_H(self,self.Ax[9000:12000]),Clustering.FFT_H(self,self.Ax[12000:15000]),Clustering.FFT_H(self,self.Ax[15000:18000]),Clustering.FFT_H(self,self.Ax[18000:21000]),Clustering.FFT_H(self,self.Ax[21000:24000]),Clustering.FFT_H(self,self.Ax[24000:27000]),Clustering.FFT_H(self,self.Ax[27000:30000]),Clustering.FFT_H(self,self.Ax[30000:33000]),Clustering.FFT_H(self,self.Ax[33000:36000]),Clustering.FFT_H(self,self.Ax[36000:39000]),Clustering.FFT_H(self,self.Ax[39000:42000])]
        
        #######################################
        #視覚課題パフォーマンス
        #######################################
        #平均
        blackout_av = [np.average(self.blackout[6000:9000]),np.average(self.blackout[9000:12000]),np.average(self.blackout[12000:15000]),np.average(self.blackout[15000:18000]),np.average(self.blackout[18000:21000]),np.average(self.blackout[21000:24000]),np.average(self.blackout[24000:27000]),np.average(self.blackout[27000:30000]),np.average(self.blackout[30000:33000]),np.average(self.blackout[33000:36000]),np.average(self.blackout[36000:39000]),np.average(self.blackout[39000:42000])]
        wakimi_av = [time_flag_blackout[(0 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 30)].mean(),time_flag_blackout[(30 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 60)].mean(),time_flag_blackout[(60 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 90)].mean(),time_flag_blackout[(90 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 120)].mean(),time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 150)].mean(),time_flag_blackout[(150 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)].mean(),time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 210)].mean(),time_flag_blackout[(210 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)].mean(),time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 270)].mean(),time_flag_blackout[(270 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)].mean(),time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 330)].mean(),time_flag_blackout[(330 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)].mean()]
        wakimi_sd = [time_flag_blackout[(0 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 30)].std(),time_flag_blackout[(30 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 60)].std(),time_flag_blackout[(60 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 90)].std(),time_flag_blackout[(90 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 120)].std(),time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 150)].std(),time_flag_blackout[(150 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)].std(),time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 210)].std(),time_flag_blackout[(210 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)].std(),time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 270)].std(),time_flag_blackout[(270 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)].std(),time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 330)].std(),time_flag_blackout[(330 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)].std()]
        wakimi_max = [time_flag_blackout[(0 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 30)].max(),time_flag_blackout[(30 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 60)].max(),time_flag_blackout[(60 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 90)].max(),time_flag_blackout[(90 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 120)].max(),time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 150)].max(),time_flag_blackout[(150 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)].max(),time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 210)].max(),time_flag_blackout[(210 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)].max(),time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 270)].max(),time_flag_blackout[(270 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)].max(),time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 330)].max(),time_flag_blackout[(330 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)].max()]
        wakimi_min = [time_flag_blackout[(0 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 30)].min(),time_flag_blackout[(30 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 60)].min(),time_flag_blackout[(60 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 90)].min(),time_flag_blackout[(90 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 120)].min(),time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 150)].min(),time_flag_blackout[(150 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)].min(),time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 210)].min(),time_flag_blackout[(210 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)].min(),time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 270)].min(),time_flag_blackout[(270 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)].min(),time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 330)].min(),time_flag_blackout[(330 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)].min()]
#blackout_FFT_L = [Clustering.FFT_ex(self,self.blackout[6000:9000]),Clustering.FFT_ex(self,self.blackout[9000:12000]),Clustering.FFT_ex(self,self.blackout[12000:15000]),Clustering.FFT_ex(self,self.blackout[15000:18000]),Clustering.FFT_ex(self,self.blackout[18000:21000]),Clustering.FFT_ex(self,self.blackout[21000:24000]),Clustering.FFT_ex(self,self.blackout[24000:27000]),Clustering.FFT_ex(self,self.blackout[27000:30000]),Clustering.FFT_ex(self,self.blackout[30000:33000]),Clustering.FFT_ex(self,self.blackout[33000:36000]),Clustering.FFT_ex(self,self.blackout[36000:39000]),Clustering.FFT_ex(self,self.blackout[39000:42000])]
        
        #out = [IVD_min,IVD_max,IVD_av,IVD_sd,Ax_min,Ax_max,Ax_av,Ax_sd,Ax_freq_acc,Ax_freq_dec,Steer_min,Steer_max,Steer_av,Steer_sd,Steer_FFT_L,Steer_FFT_H]
        out = [IVD_min,Ax_min,Ax_max,Ax_sd,Ax_freq_acc,Ax_freq_dec,Steer_min,Steer_max,Steer_sd,Steer_FFT_L,Steer_FFT_H,blackout_av,wakimi_av,wakimi_sd,wakimi_max,wakimi_min]
        return out
    
    def FFT_ex(self,data):
        # parameters
        N = 3000 # data number
        dt = 0.01
        t = np.arange(0, N*dt, dt)
        freq = np.linspace(0, 1.0/dt, N) # frequency step
        data_fft = np.abs(fft(data)/(N/2)) # 離散フーリエ変換&規格化
        plt.figure(2)
        plt.subplot(211)
        plt.plot(t, data)
        plt.xlim(0, 30)
        plt.xlabel("time")
        plt.ylabel("amplitude")
        
        plt.subplot(212)
        plt.plot(freq, np.abs(data_fft))
        plt.xlim(0, 30)
        #plt.ylim(0, 5)
        plt.xlabel("frequency")
        plt.ylabel("amplitude")
        plt.tight_layout()
        plt.savefig("01")
        plt.show()
        return np.average(data_fft[0:300])
        
    def FFT_L(self,data):
        # parameters
        N = 3000 # data number
        data_fft = np.abs(fft(data)/(N/2)) # 離散フーリエ変換&規格化
        return np.average(data_fft[0:300])
    
    def FFT_H(self,data):
        # parameters
        N = 3000 # data number
        data_fft = np.abs(fft(data)/(N/2)) # 離散フーリエ変換&規格化
        return np.average(data_fft[300:3000])
# =============================================================================
# calculationクラス
# =============================================================================
class Calculation:
    def __init__(self, data):
        self.data = data
        self.Time,self.X,self.Y,self.X_obj,self.Y_obj,self.Vx,self.Vy,self.V_obj,self.blackout,self.Ax,self.Ay,self.steer,self.throttle,self.thr_eng,self.ELSE = np.hsplit(self.data,[1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    
    def cal_BR(self):
        return np.average(self.blackout[6000:42000])
    
    def cal_a(self):
        return np.std(self.Ay[6000:42000])
    
    def cal_d(self):
        """先行車との距離計算"""
        IVD_Y = self.Y - self.Y_obj
        IVD_X = self.X_obj - self.X
        IVD = np.sqrt(np.square(IVD_X) + np.square(IVD_Y))
        
        """Carsimのバグ消去"""
        for i in range(IVD.shape[0]):
            if IVD[i] > 200:
                IVD_X[i],IVD_Y[i],IVD[i] = IVD_X[i-1],IVD_Y[i-1],IVD[i-1]
        IVD_Y = IVD_Y + 0.25
        return np.max(np.abs(IVD_Y[6000:42000]))
    
    def t_welch(self,sbject_name,task,A,B):
        A_var = np.var(A, ddof=1)  # Aの不偏分散
        B_var = np.var(B, ddof=1)  # Bの不偏分散
        A_df = len(A) - 1  # Aの自由度
        B_df = len(B) - 1  # Bの自由度
        f = A_var / B_var  # F比の値
        one_sided_pval1 = stats.f.cdf(f, A_df, B_df)  # 片側検定のp値 1
        one_sided_pval2 = stats.f.sf(f, A_df, B_df)   # 片側検定のp値 2
        two_sided_pval = min(one_sided_pval1, one_sided_pval2) * 2  # 両側検定のp値
        
        #print(sbject_name+" - "+task)
        print('F:       ', round(f, 3))
        print('p-value: ', round(two_sided_pval, 4))
        print(stats.ttest_ind(A, B, equal_var=False))
    
    #運転パフォーマンスの表示    
    def others(self,folder_name,sbject_name,task):
        fig = plt.figure(facecolor="w",figsize=(6, 2))
        plt.rcParams["font.size"] = 15
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.xlim(0, 360)
        plt.xticks([0, 60, 120, 180, 240, 300, 360])
        plt.ylim(-1, 1)
        plt.yticks([-1, 1])
        ax = fig.add_subplot(111)
        ax.plot(self.Time[0:36000],self.Ax[6000:42000],'black')
        #ax.set_xlabel("time[s]")
        #ax.set_ylabel("Ax[m/s2]")
        # 解像度を指定して保存
        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/ax_" + task + ".png", format="png", dpi=300)
        
        fig = plt.figure(facecolor="w",figsize=(6, 2))
        plt.rcParams["font.size"] = 15
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.xlim(0, 360)
        plt.xticks([0, 60, 120, 180, 240, 300, 360])
        plt.ylim(-0.1, 0.1)
        plt.yticks([-0.1, 0.1])
        ax = fig.add_subplot(111)
        ax.plot(self.Time[0:36000],self.Ay[6000:42000],'black')
        #ax.set_xlabel("time[s]")
        #ax.set_ylabel("Ay[m/s2]")
        # 解像度を指定して保存
        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/ay_" + task + ".png", format="png", dpi=300)
        
        fig = plt.figure(facecolor="w",figsize=(6, 2))
        plt.rcParams["font.size"] = 15
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.xlim(0, 360)
        plt.xticks([0, 60, 120, 180, 240, 300, 360])
        plt.ylim(-10, 10)
        plt.yticks([-10, 10])
        ax = fig.add_subplot(111)
        ax.plot(self.Time[0:36000],self.steer[6000:42000],'black')
        #ax.set_xlabel("time[s]")
        #ax.set_ylabel("steer[deg]")
        # 解像度を指定して保存
        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/steer_" + task + ".png", format="png", dpi=300)

        fig = plt.figure(facecolor="w",figsize=(6, 2))
        plt.rcParams["font.size"] = 15
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.xlim(0, 360)
        plt.xticks([0, 60, 120, 180, 240, 300, 360])
        plt.ylim(0, 1)
        plt.yticks([0, 1])
        ax = fig.add_subplot(111)
        ax.plot(self.Time[0:36000],self.throttle[6000:42000],'black')
        #ax.set_xlabel("time[s]")
        #ax.set_ylabel("throttle")
        # 解像度を指定して保存
        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/throttle_" + task + ".png", format="png", dpi=300)
    
    #微分計算
    def diff4(x, h):
        res = -x[4:] + 8*x[3:-1] - 8*x[1:-3] + x[:-4]
        return res/(12*h)
    
    def cal_d_performance_20210206(self):
        """先行車との距離計算"""
        IVD_Y = self.Y - self.Y_obj
        IVD_X = self.X_obj - self.X
        IVD = np.sqrt(np.square(IVD_X) + np.square(IVD_Y))
        
        """Carsimのバグ消去"""
        for i in range(IVD.shape[0]):
            if IVD[i] > 200:
                IVD_X[i],IVD_Y[i],IVD[i] = IVD_X[i-1],IVD_Y[i-1],IVD[i-1]
        IVD_Y = IVD_Y + 0.25
                
        #先行車時間
        time_to_collision = IVD/self.Vx
        #躍度
        Jerk_x = Calculation.diff4(self.Ax,0.01)
        Jerk_xp = np.power(Jerk_x,2)
        Jerk_y = Calculation.diff4(self.Ay,0.01)
        Jerk_yp = np.power(Jerk_y,2)
        #加速，減速頻度の計算
        ax_p = np.where(self.Ax > 0, 1, 0)
        ax_m = np.where(self.Ax < 0, 1, 0)
        flag_ax_p = np.diff(ax_p,axis = 0)
        flag_ax_m = np.diff(ax_m,axis = 0)
        #急加速，急減速頻度の計算
#        ax_pp = np.where(self.Ax > 0.1, 1, 0)
#        ax_mm = np.where(self.Ax < -0.3, 1, 0)
#        flag_ax_pp = np.diff(ax_pp,axis = 0)
#        flag_ax_mm = np.diff(ax_mm,axis = 0)
        #y加速度最大
        Steer = np.abs(self.steer)
        V_Steer = 100 * np.diff(Steer, n=1 ,axis=0)

        data1 = np.std(IVD[6001:42000])
        data2 = np.std(time_to_collision[6001:42000])
        data3 = np.max(self.Ax[6001:42000])
        data4 = np.abs(np.min(self.Ax[6001:42000]))
        data5 = np.sum(flag_ax_p[6001:42000] == -1)
        data6 = np.sum(flag_ax_m[6001:42000] == -1)
        data7 = np.sum(Jerk_xp[6001:42000])
        data8 = np.max(self.throttle[6001:42000])
        
        data9 = np.std(IVD_Y[6001:42000])
        data10 = np.max(np.abs(IVD_Y[6001:42000]))
        data11 = np.std(self.Ay[6001:42000])
        data12 = np.max(np.abs(self.Ay[6001:42000]))
        data13 = np.sum(Jerk_yp[6001:42000])
        data14 = np.std(self.steer[6001:42000])
        data15 = np.max(Steer[6001:42000])
        data16 = np.max(V_Steer[6001:42000])
        out = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16]
        return out

    def cal_v_performance_20210206(self):
        blackout = self.blackout.reshape([self.blackout.shape[0]])
        #窓枠の変更
        i = 30
        I = 10*(i+1)
        A = np.full(I,1/I)
        rateblackout = np.convolve(blackout,A,mode='same')
        rateblackout = rateblackout.reshape([self.blackout.shape[0],1])
        return rateblackout
    #IVD,LLD計算
    def cal_d_performance(self,folder_name,sbject_name,task):
        """先行車との距離計算"""
        IVD_Y = self.Y - self.Y_obj
        IVD_X = self.X_obj - self.X
        IVD = np.sqrt(np.square(IVD_X) + np.square(IVD_Y))
        
        """Carsimのバグ消去"""
        for i in range(IVD.shape[0]):
            if IVD[i] > 200:
                IVD_X[i],IVD_Y[i],IVD[i] = IVD_X[i-1],IVD_Y[i-1],IVD[i-1]
        IVD_Y = IVD_Y + 0.25
                
        #先行車時間
        time_to_collision = IVD/self.Vx

        #加速，減速頻度の計算
        #ax_p = np.where(self.Ax > 0, 1, 0)
        #ax_m = np.where(self.Ax < 0, 1, 0)
        #flag_ax_p = np.diff(ax_p,axis = 0)
        #flag_ax_m = np.diff(ax_m,axis = 0)
        #急加速，急減速頻度の計算
        ax_pp = np.where(self.Ax > 0.1, 1, 0)
        ax_mm = np.where(self.Ax < -0.3, 1, 0)
        flag_ax_pp = np.diff(ax_pp,axis = 0)
        flag_ax_mm = np.diff(ax_mm,axis = 0)
        #y加速度最大
        Ay = abs(self.Ay)
        Steer = abs(self.steer)
        V_Steer = 100 * np.diff(Steer, n=1 ,axis=0)
        #######################################
        ##縦方向パフォーマンス
        #######################################
        #二乗平均平方根誤差 (RMSE)
        #data_1 = [np.sqrt(mean_squared_error(self.Vx[12001:18000], self.V_obj[12001:18000])),np.sqrt(mean_squared_error(self.Vx[18001:24000], self.V_obj[18001:24000])),np.sqrt(mean_squared_error(self.Vx[24001:30000], self.V_obj[24001:30000])),np.sqrt(mean_squared_error(self.Vx[30001:36000], self.V_obj[30001:36000])),np.sqrt(mean_squared_error(self.Vx[6001:12000], self.V_obj[6001:12000])),np.sqrt(mean_squared_error(self.Vx[36001:42000], self.V_obj[36001:42000]))]
        data_1 = [np.min(IVD[6001:12000]),np.min(IVD[12001:18000]),np.min(IVD[18001:24000]),np.min(IVD[24001:30000]),np.min(IVD[30001:36000]),np.min(IVD[36001:42000])]


        #先行車時間 MIN
        data_2 = [np.min(time_to_collision[6001:12000]),np.min(time_to_collision[12001:18000]),np.min(time_to_collision[18001:24000]),np.min(time_to_collision[24001:30000]),np.min(time_to_collision[30001:36000]),np.min(time_to_collision[36001:42000])]
        
        #加速，減速 MAX
        data_3 = [np.max(self.Ax[6001:12000]),np.max(self.Ax[12001:18000]),np.max(self.Ax[18001:24000]),np.max(self.Ax[24001:30000]),np.max(self.Ax[30001:36000]),np.max(self.Ax[36001:42000])]        
        data_4 = [np.min(self.Ax[6001:12000]),np.min(self.Ax[12001:18000]),np.min(self.Ax[18001:24000]),np.min(self.Ax[24001:30000]),np.min(self.Ax[30001:36000]),np.min(self.Ax[36001:42000])]
        
        #急加速（減速）頻度
        data_5 = [np.sum(flag_ax_pp[6001:12000] == -1),np.sum(flag_ax_pp[12001:18000] == -1),np.sum(flag_ax_pp[18001:24000] == -1),np.sum(flag_ax_pp[24001:30000] == -1),np.sum(flag_ax_pp[30001:36000] == -1),np.sum(flag_ax_pp[36001:42000] == -1)]
        data_6 = [np.sum(flag_ax_mm[6001:12000] == -1),np.sum(flag_ax_mm[12001:18000] == -1),np.sum(flag_ax_mm[18001:24000] == -1),np.sum(flag_ax_mm[24001:30000] == -1),np.sum(flag_ax_mm[30001:36000] == -1),np.sum(flag_ax_mm[36001:42000] == -1)]
        #加速（減速）頻度
        #data_6 = [np.sum(flag_ax_p[6001:12000] == -1),np.sum(flag_ax_p[12001:18000] == -1),np.sum(flag_ax_p[18001:24000] == -1),np.sum(flag_ax_p[24001:30000] == -1),np.sum(flag_ax_p[30001:36000] == -1),np.sum(flag_ax_p[36001:42000] == -1)]
        #data_7 = [np.sum(flag_ax_m[6001:12000] == -1),np.sum(flag_ax_m[12001:18000] == -1),np.sum(flag_ax_m[18001:24000] == -1),np.sum(flag_ax_m[24001:30000] == -1),np.sum(flag_ax_m[30001:36000] == -1),np.sum(flag_ax_m[36001:42000] == -1)]

        #######################################
        ##横方向パフォーマンス
        #######################################
        #車線逸脱 SD MAX MIN
        data_7 = [np.std(IVD_Y[6001:12000]),np.std(IVD_Y[12001:18000]),np.std(IVD_Y[18001:24000]),np.std(IVD_Y[24001:30000]),np.std(IVD_Y[30001:36000]),np.std(IVD_Y[36001:42000])]        
        data_8 = [np.max(IVD_Y[6001:12000]),np.max(IVD_Y[12001:18000]),np.max(IVD_Y[18001:24000]),np.max(IVD_Y[24001:30000]),np.max(IVD_Y[30001:36000]),np.max(IVD_Y[36001:42000])]
        data_9 = [np.min(IVD_Y[6001:12000]),np.min(IVD_Y[12001:18000]),np.min(IVD_Y[18001:24000]),np.min(IVD_Y[24001:30000]),np.min(IVD_Y[30001:36000]),np.min(IVD_Y[36001:42000])]
        #横加速度 MAX
        data_10 = [np.max(Ay[6001:12000]),np.max(Ay[12001:18000]),np.max(Ay[18001:24000]),np.max(Ay[24001:30000]),np.max(Ay[30001:36000]),np.max(Ay[36001:42000])]
        #ステアリング角度 MAX
        data_11 = [np.max(Steer[6001:12000]),np.max(Steer[12001:18000]),np.max(Steer[18001:24000]),np.max(Steer[24001:30000]),np.max(Steer[30001:36000]),np.max(Steer[36001:42000])]
        #ステアリング速度 MAX
        data_12 = [np.max(V_Steer[6001:12000]),np.max(V_Steer[12001:18000]),np.max(V_Steer[18001:24000]),np.max(V_Steer[24001:30000]),np.max(V_Steer[30001:36000]),np.max(V_Steer[36001:42000])]
        """配列の結合"""
        out = [data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,data_10,data_11,data_12]
        return out

    #平均わき見（blackout）時間，totalわき見(bkackout)回数
    def cal_v_performance(self,folder_name,sbject_name,task):
        #形式変更
        time = self.Time.reshape([self.Time.shape[0],1])
        time = time - 60
        self.blackout[0] = 1
        blackout = np.append(self.blackout,1)
        #差分計算（立ち上がりが1，立下りが-1）
        #print(self.blackout.shape)
        flag_blackout = np.diff(blackout,axis = 0)
        #末尾に0を追加
        #flag_blackout = np.append(flag_blackout,0)
        #print(flag_blackout.shape)
        
        #わき見頻度
        #print(np.sum(flag_blackout == -1))
        #わき見時間（-1～1の時間？？）
        time_flag_blackout_p1 = time[flag_blackout == 1]
        time_flag_blackout_m1 = time[flag_blackout == -1]
        time_flag_blackout = time_flag_blackout_p1 - time_flag_blackout_m1
        #out = np.concatenate((time_flag_blackout_p1,time_flag_blackout),axis = 1)
        a1,a2,a3,a4,a5,a6 = time_flag_blackout[(0 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 60)].mean(),time_flag_blackout[(60 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 120)].mean(),time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)].mean(),time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)].mean(),time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)].mean(),time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)].mean()
        std1,std2,std3,std4,std5,std6 = time_flag_blackout[(0 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 60)].std(),time_flag_blackout[(60 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 120)].std(),time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)].std(),time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)].std(),time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)].std(),time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)].std()
        data_1 = [a1,a2,a3,a4,a5,a6]
        data_1_std = [std1,std2,std3,std4,std5,std6]
        
        #検定###########################################################################################
#        B_3 = time_flag_blackout[(120 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 180)]
#        B_4 = time_flag_blackout[(180 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 240)]
#        B_5 = time_flag_blackout[(240 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 300)]
#        B_6 = time_flag_blackout[(300 < time_flag_blackout_p1) & (time_flag_blackout_p1 < 360)]
#        print(sbject_name+" - "+task)
#        print(data_1)
#        print("3-4")
#        Calculation.t_welch(self,sbject_name,task,B_3,B_4)
#        print("3-5")
#        Calculation.t_welch(self,sbject_name,task,B_3,B_5)
#        print("3-6")
#        Calculation.t_welch(self,sbject_name,task,B_3,B_6)
        ################################################################################################
        
        
#        # 平均わき見　##################################################################################
#        fig = plt.figure(facecolor="w",figsize=(6, 2))
#        plt.rcParams["font.size"] = 15
#        plt.rcParams['font.family'] = 'Times New Roman'
#        plt.xlim(0, 360)
#        plt.xticks([0, 60, 120, 180, 240, 300, 360])
#        plt.ylim(0, 5)
#        plt.yticks([0, 5])
#        ax = fig.add_subplot(111)
#        ax.plot(time_flag_blackout_p1,time_flag_blackout,'black')
#        #ax.set_xlabel("time[s]")
#        #ax.set_ylabel("no_blackout[s]")
#        # 解像度を指定して保存
#        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/blackout_" + task + ".png", format="png", dpi=300)
        data_2, data_2_std = Calculation.rate_blackout_wavelet(self,folder_name,sbject_name,task,31)
        data = [data_1,data_1_std,data_2,data_2_std]
        #std = [data_1_std,data_2_std]
        return data
    
    #blackout率の計算（移動平均）
    def rate_blackout_wavelet(self,folder_name,sbject_name,task,para):
        """畳み込み"""
        #形式変更
        blackout = self.blackout.reshape([self.blackout.shape[0]])
        blackout_wavelet = self.blackout
        #窓枠の変更
        #0.1～5.0秒の窓枠
        for i in range(50):
            I = 10*(i+1)
            A = np.full(I,1/I)
            rateblackout = np.convolve(blackout,A,mode='same')
            rateblackout = rateblackout.reshape([self.blackout.shape[0],1])
            blackout_wavelet = np.append(blackout_wavelet,rateblackout, axis = 1)
        #print(blackout_wavelet.shape)
        
#        # blackout rate##################################################################################
#        fig = plt.figure(facecolor="w",figsize=(6, 2))
#        plt.rcParams["font.size"] = 15
#        plt.rcParams['font.family'] = 'Times New Roman'
#        plt.xlim(0, 360)
#        plt.xticks([0, 60, 120, 180, 240, 300, 360])
#        plt.ylim(0, 100)
#        plt.yticks([0, 100])
#        ax = fig.add_subplot(111)
#        ax.plot(self.Time[0:36000],100*blackout_wavelet[6000:42000,para],'black')
#        #ax.set_xlabel("time[s]")
#        #ax.set_ylabel("blackout[%]")
#        # 解像度を指定して保存
#        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/av_blackout_" + task + ".png", format="png", dpi=300)
#        
#        # blackout rate・棒グラフ　##################################################################################
#        fig, ax = plt.subplots(figsize=(3, 4))
#        ax.axes.xaxis.set_visible(False)
#        plt.ylim(0, 100)
#        plt.yticks([0, 100])
#        no_ = [1,2]
#        data_ = [100*np.average(blackout_wavelet[6000:24000,para]),100*np.average(blackout_wavelet[24000:42000,para])]
#        yeer = [100*np.std(blackout_wavelet[6000:24000,para]),100*np.std(blackout_wavelet[24000:42000,para])]
#        plt.bar(no_, data_, yerr=yeer, ecolor="black",color="gray",width=0.7)
#        plt.savefig("./" + folder_name + "/output/" + sbject_name + "/bar_av_blackout_" + task + ".png", format="png", dpi=300)
#        #print(100*np.average(blackout[6000:42000]))
#        
        #print(100*np.average(blackout_wavelet[6000:24000,para]))
        #print(100*np.std(blackout_wavelet[6000:24000,para]))
        
        #print(100*np.average(blackout_wavelet[24000:42000,para]))
        #print(100*np.std(blackout_wavelet[24000:42000,para]))

        
#        """配列の結合"""
#        graf = blackout_wavelet.T
#        #graf[graf>0.01]=1
#        plt.figure(figsize=(32, 16))
#        plt.rcParams["font.size"] = 30
#        sns.heatmap(graf[:,1:24001],xticklabels=6000,yticklabels=10)
#        plt.savefig("20191129_ito.png")
#        plt.close('all')
        
        #検定##############################################################################
#        A_1 = blackout_wavelet[18000:24000,para]
#        B_1 = blackout_wavelet[24000:30000,para]
#        Calculation.t_welch(self,sbject_name,task,A_1,B_1)
        ###################################################################################
        
        data = [100*np.average(blackout_wavelet[6000:12000,para]),100*np.average(blackout_wavelet[12000:18000,para]),100*np.average(blackout_wavelet[18000:24000,para]),100*np.average(blackout_wavelet[24000:30000,para]),100*np.average(blackout_wavelet[30000:36000,para]),100*np.average(blackout_wavelet[36000:42000,para])]
        data_std = [100*np.std(blackout_wavelet[6000:12000,para]),100*np.std(blackout_wavelet[12000:18000,para]),100*np.std(blackout_wavelet[18000:24000,para]),100*np.std(blackout_wavelet[24000:30000,para]),100*np.std(blackout_wavelet[30000:36000,para]),100*np.std(blackout_wavelet[36000:42000,para])]
#        out = np.concatenate((self.Time,blackout_wavelet), axis = 1)
        print(sbject_name+" - "+task)
        AV_d = 100*np.average(blackout_wavelet[6000:24000,para])
        print(AV_d - data[3],AV_d - data[4],AV_d - data[5])
        return data,data_std
        #return blackout_wavelet[:,para]