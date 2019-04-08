set encoding utf8
set yrange[-2:2]
set xrange[-2:2]
set title "SBX"
#set key outside
unset key
set term post color 2
set terminal png
set xlabel "x1"
set ylabel "x2"
set view 60,40
set output "SBX_eta_2.png"
plot "SBX_eta_2" 

set title "SBX"
#set key outside
unset key
set yrange[-2:2]
set xrange[-2:2]
set term post color 18
set ter png
set xlabel "x1"
set ylabel "x2"
set view 60,40
set output "SBX_eta_20_2D.png"
plot "SBX_eta_20_2D" 

set encoding utf8
set yrange[-2:2]
set xrange[-2:2]
set zrange[-2:2]
set title "SBX"
#set key outside
unset key
set term post color 2
set terminal png
set xlabel "x1"
set ylabel "x2"
set zlabel "x3"
set view 60,40
set output "SBX_eta_20_3D.png"
splot "SBX_eta_20_3D"

set encoding utf8
set yrange[-2:2]
set xrange[-2:2]
set title "SBX"
#set key outside
unset key
set term post color 2
set terminal png
set xlabel "x1"
set ylabel "x2"
set view 60,40
set output "SBX_eta_20_2D_pv_1.png"
plot "SBX_eta_20_2D_pv_1" 

set title "SBX"
#set key outside
unset key
set yrange[-2:2]
set xrange[-2:2]
set term post color 18
set ter png
set xlabel "x1"
set ylabel "x2"
set view 60,40
set output "SBX_eta_20_2D_pv_01.png"
plot "SBX_eta_20_2D_pv_01" 

