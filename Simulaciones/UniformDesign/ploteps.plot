set encoding utf8
#set yrange[0:0.5]
set title "Diseño simplex-lattice"
#set key outside
unset key
set term post color 18
set xlabel "w1"
set ylabel "w2"
set zlabel "w3"
set view 40,65
set output "simplex.eps"
splot "weight_03D_13.sld", "lines" with lines;

#set yrange[0:0.8]
set title "Diseño uniforme"
#set key outside
unset key
set term post color 18
set xlabel "w1"
set ylabel "w2"
set zlabel "w3"
set view 40,65
set output "uniforme.eps"

splot "Uniform3D-105.dat", "lines" with lines;

#set yrange[0:0.8]
set title "Diseño uniforme"
#set key outside
unset key
set term post color 18
set xlabel "w1"
set ylabel "w2"
set zlabel "w3"
set view 40,65
set output "uniform.eps"

splot "Uniform_Extremes.dat", "lines" with lines;


