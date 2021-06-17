# 0800-fizobl-metadynamics
Drugi projekt z Fizyki Obliczeniowej

Celem projektu było wykonanie symulacji zachowania pojedynczej molekuły NaCl w wodnym roztworze i jej analiza metodami metadynamiki przy użyciu probramów LAMMPS oraz PLUMED. Pliki użyte w do symulacji znajdują się w repozytorium
![project-2](https://github.com/jakryd/0800-fizobl/tree/main/project-2/irtg-school-mainz-2020-metad).

Symulacja odbywała się w temperaturze 300 K i trwała 10 ns. Wykorzystano w niej potencjał obciążający postaci

![V](https://latex.codecogs.com/svg.image?V(d)=-\left(1-\frac{1}{\gamma}\right)F(d),)

co prowadzi do efektywnej energii swobodnej

![F](https://latex.codecogs.com/svg.image?F(d)/\gamma,)

a więc bariery energii swobodnej obniżone są o czynnik ![gamma](https://latex.codecogs.com/svg.image?\gamma), który dobrano tak, aby były one rzędu kilku kT.

Wygenerowane w symulacji powierzchnie energii swobodnej w kolejnych momentach trwania symulacji przedstawiono na wykresie 1:
![free_energy_metadynamics.png](https://raw.githubusercontent.com/adamzny/0800-fizobl-metadynamics/main/free_energy_metadynamics.png)
gdzie krzywe przesunięto tak, by minimum energii swobodnej miało wartość 0. Jak widać, pod koniec symulacji krzywe są coraz bliżej siebie, co świadczy o jej zbieżności. Z wykresu można odczytać dwa lokalne minima energii swobodnej - płytsze dla odległości ok. 0.26 nm odpowiadające stanowi związanemu NaCl i nieco głębsze oraz znacznie szersze odpowiadające stanowi zdysocjowanemu. Minima rozdziela bariera potencjalna o wysokości około 4 kT.
Powyżej ok. 6 nm wartości energii swobodnej gwałtownie rosną, nie jest to jednak efekt fizyczny, a jedynie ograniczenie symulacji - w celu ograniczenia przestrzeni próbkowania potencjał modyfikowany jest o człon o kształcie dodatniej gałęzi paraboli:

![V_w](https://latex.codecogs.com/svg.image?V_w(d)=\kappa(d-0.6)^2,\qquad&space;d>0.6,)

Aby pozbyć się tego efektu zastosowano tzw. *reweighting*, czyli zmodyfikowano uzyskany profil energii swobodnej wagami postaci

![weights](https://latex.codecogs.com/svg.image?\exp\left[\beta\left(V(d,t)-c(t)+V_w(d)\right)\right].)

Porównanie otrzymanej krzywej energii swobodnej z tą otrzymaną na koniec symulacji przed ważeniem przedstawia wykres 2:
![comparison.png](https://raw.githubusercontent.com/adamzny/0800-fizobl-metadynamics/main/comparison.png)

Zastosowana metoda skuteczne usunęła niefizyczną barierę jddnocześnie zachowując kształt pozostałej części profilu energii swobodnej.
