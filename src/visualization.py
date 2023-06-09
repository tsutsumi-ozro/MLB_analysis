import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

class Plotter:
    DIAMOND_X_M = [0, -19.2, 0, 19.2,0]
    DIAMOND_Y_M = [0, 19.2, 38.4, 19.2, 0]

    def plot_ball_direction(self, df):
        df['norm_hc_x'] = (df['hc_x'] - 125.42) * 2.5 * 0.3048 # ホームベース地点を0とし、mへ変換
        df['norm_hc_y'] = (198.27 - df['hc_y']) * 2.5 * 0.3048
        fig = px.scatter(
            df.sort_values('events'), # events(打席結果)でsort. 文字順なのでdoubleが先頭
            x="norm_hc_x",
            y="norm_hc_y",
            color='events',
            # hover_nameでマウスオーバー時に表示するカラムを指定
            hover_name="events", hover_data=["pitcher", "pitch_name"]
            )
        # 内野の描画
        fig.add_trace(go.Scatter(
            name='diamond',
            x=self.DIAMOND_X_M,
            y=self.DIAMOND_Y_M,
            fillcolor='darkviolet',
            line_color='black')
        )
        # フェアゾーンのライン
        fig.add_trace(go.Scatter(
            name='line',
            x=[-100, 0, 100],
            y=[100, 0, 100],
            fillcolor='darkviolet',
            line_color='black',)
        )
        fig.update_layout(
            title='Batting, Location',
            autosize=False,
            width=800,
            height=600,
        )
        fig.update_xaxes(range=[-100 , 100], title='hc_x(m)', dtick=40)
        fig.update_yaxes(range=[0, 160], title='hc_y(m)', dtick=40)
        fig.show()

    def plot_events(self, df):
        events = df['events'].dropna().value_counts()
        fig = go.Figure(data=[go.Pie(labels=events.index, values=events.values)])
        fig.update_layout(
            title='Batting, Events',
            autosize=False,
            width=800,
            height=600,
        )
        fig.show()

