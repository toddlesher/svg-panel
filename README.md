Create soldermask and silkscreen layers for a front panel PCB.

Given label names, label x/y centers, and label widths and heights, create solid boxes from which text is subtracted.

Silkscreen is, by default, not added over bare copper. Add the soldermask layer so the silk has somewhere to be.

TODO:
* subtract text from boxes
* add soldermask under all silk
* add three-state labels and lines
* add an `OFF L R L+R START` round plate
* add kicad cam out actions

![image](https://github.com/user-attachments/assets/8ffa4dcd-2f74-46e7-8781-d13f96110a44)

![image](https://github.com/user-attachments/assets/905f27e3-4047-418a-bb75-670e8cb0693a)
