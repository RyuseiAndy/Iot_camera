<h1 align="center">Raspberry Piを用いたIot監視カメラ</h1>
&nbsp;

<h3 align="center">Motivation</h3>
ー   自分のアパートに友達が遊びに来た時、駐車場に車を停めて遊んでいた所、鍵傷で文字を書かれる悪戯にあったことがありました。自分の家の駐車場は治安が悪いと思ったので、物体を検知したら通知をしてくれるIoTカメラを作りたいと考えました。   

<h3 align="center">Purpose </h3>
ー  RaspberryPi3 とライブラリにあるOpenCV、Webカメラを使用し、撮影している映像に変化があった場合に検知される、動体検知カメラを作成する。

ー  また、撮影された映像がインターネットを軽有して（LINE Notify）を使用し,LINEに通知が来るようにすることが目的

<h3 align="center">Functional spec</h3>
ー  モニターには撮影した映像と時刻を表示。また、動きを検知した場合のピクセル値を表示  
ー  OpenCVを使い物体が検知されればJPEG形式で保存
ー  保存されLINE上に送信される画像にも日付、時刻、ピクセル値を表示

<h3 align="center">Creative points in My work with figures </h3>
ー  画像の閾値に輪郭線を入れることで変化がわかりやすく見やすくしました
ー  保存される画像が容量いっぱいにならないようPCのローカルディスクは上書きされるようにした点、しかしLINE上で送信される画像は物体が動き保存された画像全てを通知する点
<t></t>
<div align="center">

![px](https://user-images.githubusercontent.com/83407832/150933112-339bd8be-4259-44b7-ae16-d8cd89c08bdc.jpg)

</div>

<h3 align="left">Languages and Tools:</h3>
&nbsp;
<img src="https://img.shields.io/badge/Python-OpenCv-6F02B5.svg?logo=python&style=popout-square">
<img src="https://img.shields.io/badge/-Raspberrypi-C51A4A.svg?logo=raspberrypi&style=popout-square">
&nbsp;
