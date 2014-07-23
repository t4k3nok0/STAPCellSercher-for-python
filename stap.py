#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import datetime
import time


celllist =('A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z')
#細胞のリスト

starttime = time.clock()
#発見した時に時間を計算して出すので、開始時間を控える

print "STAP細胞をさがしてみまーすｗｗｗｗｗｗｗｗ"

time.sleep(3)
#printを表示させるためだけの停止　いらない。

while 1:
	random.choice(celllist)
	cell1 = random.choice(celllist)
	random.choice(celllist)
	cell2 = random.choice(celllist)
	random.choice(celllist)
	cell3 = random.choice(celllist)
	random.choice(celllist)
	cell4 = random.choice(celllist)
#ランダムでアルファベットを抽出する*4 もっと効率的なやり方がありそう。

	cell = str(cell1 + cell2 + cell3 +cell4)
#抽出されたアルファベット*4をひとつの文字列にする

	print cell + " 細胞"

	if cell == str("STAP"):
		endtime = time.clock()
		print "陽性確認 よかった。"
		starttime = int(starttime)
		endtime = int(endtime)
		time = endtime - starttime
		time = str(time)
		print "STAP細胞発見までに" + time + "秒かかりました"
		sys.exit()
#もしSTAPがみつかったら陽性を確認して、かかった時間を表示

	else:
		pass
 #それ以外なら上記処理を繰り返す
