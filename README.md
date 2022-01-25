<h1 align="center">:star:  Raspberry Piを用いたIot監視カメラ  :star:</h1>
&nbsp;

<h3 align="center">:seedling:  Motivation  :seedling:</h3>
ー   自分のアパートに友達が遊びに来た時、駐車場に車を停めて遊んでいた所、鍵傷で文字を書かれる悪戯にあったことがありました。自分の家の駐車場は治安が悪いと思ったので、物体を検知したら通知をしてくれるIoTカメラを作りたいと考えました。   

<h3 align="center">:herb:  Purpose  :herb:</h3>
ー  RaspberryPi3 とライブラリにあるOpenCV、Webカメラを使用し、撮影している映像に変化があった場合に検知される、動体検知カメラを作成する。

ー  また、撮影された映像がインターネットを軽有して（LINE Notify）を使用し,LINEに通知が来るようにすることが目的

<h3 align="center">:deciduous_tree:  Functional spec  :deciduous_tree:</h3>
ー  モニターには撮影した映像と時刻を表示。また、動きを検知した場合のピクセル値を表示  
ー  OpenCVを使い物体が検知されればJPEG形式で保存
ー  保存されLINE上に送信される画像にも日付、時刻、ピクセル値を表示

<h3 align="left">Languages and Tools:</h3>
&nbsp;
<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noopener"> <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"/></a> 
</p>
&nbsp;
