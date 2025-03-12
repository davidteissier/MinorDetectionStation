# **Minor Detection Station (MDS)**
*A software solution for automated minor celestial object detection and confirmation as part of the Minor Observation Network (MON).*

---

## **🌌 Vision & Purpose**
The **Minor Detection Station (MDS)** is a software system designed to autonomously monitor the night sky for **minor celestial objects**, including asteroids, comets, and other transient objects.  

Each station within the **Minor Observation Network (MON)** plays a crucial role in **detecting, tracking, and confirming** these objects, contributing valuable data to the global astronomical community.

While professional sky surveys focus on large-scale detections, MDS empowers **amateurs and independent observers** to contribute scientifically meaningful discoveries—whether by **tracking known objects** or even **making new detections** that could one day bear their names.

---

<<<<<<< HEAD
## **🛠️ Technical Stack**
- **Main Language:** Python 3
- **Image Acquisition:** 
  - pyasi (ZWO ASI camera control)
  - opencv
- **Detection & Analysis:** 
  - scikit-image
  - astropy
  - photutils
- **Astrometric Calibration:** 
  - SkyFit2
  - astropy
  - skyfield
- **Data Management:** 
  - requests
  - paramiko (SSH)
- **Web Interface:** 
  - Flask
  - Bootstrap 5
- **Target Hardware:** 
  - Raspberry Pi (all versions)
  - Linux-compatible systems

---

## **⚙️ Installation**

### Prerequisites
- Python 3.x
- ZWO ASI Camera SDK
- Git

### Quick Start
\`\`\`bash
# Clone the repository
git clone https://github.com/yourusername/MinorDetectionStation.git
cd MinorDetectionStation

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure your station
cp config.ini.example config.ini
# Edit config.ini with your station details
\`\`\`

### Web Interface
Access the web interface at \`http://localhost:5001\` to:
- Configure station parameters
- Monitor system status
- View observation logs
- Manage detections
=======
## **🛰️ How MDS Works**
✔ **A fixed ground-based station** continuously monitors a specific area of the sky.  
✔ **Each station is assigned a fixed 2° x 2° sky square** for structured sky coverage.  
✔ **Automated data acquisition** captures and analyzes images each night.  
✔ **Detects minor objects** by analyzing motion against fixed star fields.  
✔ **Confirms transits of known asteroids & comets**, assisting in refining orbital parameters.  
✔ **Triangulates detections** across multiple stations to validate discoveries.  
✔ **Filters out satellites, planes, and artifacts** to focus only on astronomical targets.  
✔ **Notifies the MON network of possible new objects**, enabling further observations.  
✔ **Collaborates with official databases**, with confirmed discoveries submitted to the **Minor Planet Center (MPC)**.  
>>>>>>> 105ddaf3a382b9575864318ff8bf5f986142f485

---

## **🔭 Fixed Station Deployment**
- The **Minor Detection Station (MDS) is designed as a fixed installation**.
- The station will be mounted on a stable **support structure** with no motorized tracking.
- Each participant will be assigned a **2° x 2° field** in the celestial grid.
- The station will automatically capture and analyze images every night.

🔧 **List of required materials and detailed construction tutorial will be provided soon!**  

---

## **🔄 How Discoveries Are Confirmed**
The detection process follows a strict **validation hierarchy**:
1. **Level 1:** A station flags an object as a "suspect".
2. **Level 2:** The same object is detected by a second station.
3. **Level 3:** Triangulation occurs with at least three independent observations.
4. **Level 4:** The object is **confirmed** as a genuine minor celestial body.
5. **Level 5:** If not previously cataloged, the object is submitted to the **Minor Planet Center (MPC)**.

---

## **🌟 Naming a New Discovery**
If an object is officially confirmed as a new celestial body and recognized by the **Minor Planet Center**, the **original discoverer** will have the privilege of naming it!  

To honor its origins within our network, all discoveries will be prefixed with **"MON"**.  
For example:  
🔹 *MON Astérix*  
🔹 *MON Voyager*  
🔹 *MON Hypatia*  

<<<<<<< HEAD
---

## **�� Join the Network**
=======
A name that could one day be immortalized in the cosmos. Will yours be next?

---

## **🌐 Join the Network**
>>>>>>> 105ddaf3a382b9575864318ff8bf5f986142f485
Whether you are an amateur astronomer, an astrophotography enthusiast, or a data scientist, you can contribute to the **Minor Observation Network (MON)**.  

By deploying a **Minor Detection Station (MDS)**, you become part of a **global effort to explore, track, and catalog** celestial objects that might otherwise go unnoticed.

<<<<<<< HEAD
---

## **📝 License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **🤝 Contributing**
Contributions are welcome! Please feel free to submit a Pull Request.

---

## **📞 Support**
For support, please open an issue in the GitHub repository or contact the MON network administrators.

🚀 *"Look beyond the stars—you may find something that no one has seen before."*
=======
Stay tuned for updates on how to participate!

🚀 *"Look beyond the stars—you may find something that no one has seen before."*
>>>>>>> 105ddaf3a382b9575864318ff8bf5f986142f485
