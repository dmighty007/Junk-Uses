#!/bin/bash
gmx solvate -cs tip4p.gro -box 2.2 2.2 2.2 -p topol.top -o water_box.gro
gmx grompp -f min.mdp -c water_box.gro -r water_box.gro -p topol.top -o min.tpr
gmx mdrun -deffnm min
gmx grompp -f min2.mdp -c min.gro -r min.gro -p topol.top -o min2.tpr
gmx mdrun -deffnm min2
gmx grompp -f eql.mdp -c min2.gro -r min2.gro -p topol.top -o eql.tpr
gmx mdrun -deffnm eql
gmx grompp -f eql2.mdp -c eql.gro -r eql.gro -t eql.cpt -p topol.top -o eql2.tpr
gmx mdrun -deffnm eql2

