# 🚦 ROADIA – Road + AI + Assistance

**ROADIA** is a simulation project exploring how Artificial Intelligence and connected systems could improve road safety and traffic flow.  
This prototype demonstrates an intelligent intersection where multiple cars drive in real time and follow different directions based on the drivers’ choices.



## 🎯 Project Goal
Today, roads face three major problems:  
- **Overspeeding** → leading cause of deadly accidents.  
- **Traffic jams** → time loss and reduced productivity.  
- **Human decisions at intersections** → frequent source of collisions.

ROADIA offers a solution: **connecting roads, cars, and AI** to assist drivers and reduce risks.



##  Demo Features
- **Intersection in the shape of a ➕ (one vertical road and one horizontal road).**  
- **Simulation of three cars in real time**:  
  - Car 1 (red) → turns left  
  - Car 2 (blue) → turns right  
  - Car 3 (green) → goes straight  
- **Predefined direction choices** → simulate the driver’s decision before the intersection.  
- Cars continue their trajectory after turning or going straight.  



## Demonstration Videos

- 🎥 **Technical demo (Pygame simulation):** [https://youtube.com/shorts/2kiXoITqzz0?si=uwB8xs7sErKv7KR0]  

- 🎥 ** Short video presentation of the features (41 seconds.  designed with Canva):** [https://youtube.com/shorts/TraFoG8Pg5c?si=6WaOCre-XIokIeN4]



## Code
The code is written in **Python** using the **Pygame** library.  
It is simple, documented, and designed to illustrate the concept, not to replace a real embedded system.  

### Example (snippet):
```python
# Each car has a "choice_direction"
# left = turn left, right = turn right, straight = go straight
car1 = Car(290, -100, RED, "left")
car2 = Car(340, -200, BLUE, "right")
car3 = Car(390, -300, GREEN, "straight")






🚀 Future Perspectives

This demo is a proof of concept.
In the future, ROADIA could integrate:

Collision detection.

Management of multiple connected intersections.

More advanced algorithms (e.g., machine learning to optimize traffic).

More realistic 3D simulations.





👤 Author

Project created by Lasme Seth Joseph Messi Emmanuel

High school senior (Terminale C), Côte d’Ivoire

Passionate about mechanics, aeronautics, and technological innovation

contact : lasmesethjosephmessi7002@gmail.com
