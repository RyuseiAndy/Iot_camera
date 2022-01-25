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

<h3 align="center">:cactus:  Creative points in My work with figures  :cactus: </h3>
ー  画像の閾値に輪郭線を入れることで変化がわかりやすく見やすくしました
ー  保存される画像が容量いっぱいにならないようPCのローカルディスクは上書きされるようにした点、しかしLINE上で送信される画像は物体が動き保存された画像全てを通知する点


<h3 align="left">Languages and Tools:</h3>
&nbsp;
<p align="left">
<a paython="https://www.python.org/" target="_blank" rel="noopener"> <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" ></a> </p>
<p align="left">
<a href="https://icons8.com/icon/s8AQ7pC6ux27/raspberry-pi-is-a-small-and-affordable-computer-that-you-can-use-to-learn-programming">Raspberry Pi is a small and affordable computer that you can use to learn programming icon by Icons8</a>
<a ras="https://www.raspberrypi.org/" target="_blank" rel="noopener"> "<img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/24/000000/external-raspberry-pi-is-a-small-and-affordable-computer-that-you-can-use-to-learn-programming-logo-shadow-tal-revivo.png">"/></a> </p>
<p align="left">
<a line="https://notify-bot.line.me/ja/" target="_blank" rel="noopener"> <img src= "https://img.icons8.com/color/48/000000/line-me.png"/></a> </p>


</p>
&nbsp;
