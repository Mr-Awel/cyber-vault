![[OSI Model Diagram.png]]
-The **OSI** model (or **O**pen **S**ystems **I**nterconnection Model) is an essential model used in networking.  This critical model provides a framework dictating how all networked devices will send, receive and interpret data.

-**Physical** layer is one of the easiest layers to grasp. Put simply, this layer references the physical components of the hardware used in networking and is the lowest layer that you will find. Devices use electrical signals to transfer data between each other in a binary numbering system (1's and 0's).

-**Data link** layer focuses on the physical addressing of the transmission. It's the job of the data link layer to present the data in a format suitable for transmission.

-**Network** layer of the OSI model is where the magic of routing & re-assembly of data takes place (from these small chunks to the larger chunk). The protocols at this layer like **OSPF** (**O**pen **S**hortest **P**ath **F**irst) and **RIP** (**R**outing **I**nformation **P**rotocol) determine the optimal path should take to reach a device. 

-**Transport** Layer hands off a stream or datagram from the application into numbered chunks tagged with port info; **TCP** turns those into a reliable, in-order byte stream using handshakes, ACKs, and windowing, while **UDP** simply pushes each packet out with minimal fuss, trading reliability for speed.

-**Session** Layer sets up, labels, and tears down each “conversation” between applications, tracking who’s talking to whom, enforcing turn-taking if needed, and dropping back to the last checkpoint on failure, before handing reliable data streams off to Layer 4(Transport).

-**Presentation** Layer makes sure that, no matter what formats or encryption each application uses, the data is packaged into a common, compressed/encrypted “lingua franca” before it goes down to Transport (and unpacks back up on the far side).

----------------------------------
## **Questions**

What does the "OSI" in "OSI Model" stand for?
**=Open Systems Interconnection**

How many layers (in digits) does the OSI model have?
**=7**

What is the key term for when pieces of information get added to data?
**=Encapsulation**

What is the name of this Layer(1)?
**=Physical**

What is the name of the numbering system that is both 0's and 1's?
**=Binary**

What is the name of the cables that are used to connect devices?
**=Ethernet Cables**

What is the name of this Layer(2)?
**=Data Link**

What is the name of the piece of hardware that all networked devices come with?
**=Network Interface Card**

What is the name of this Layer(3)?
**=Network**

Will packets take the most optimal route across a network? (Y/N)
**=Y**

What does the acronym "OSPF" stand for?
**=Open Shortest Path First**

What does the acronym "RIP" stand for?
**=Routing Information Protocol**

What type of addresses are dealt with at this layer?
**=IP Addresses**

What is the name of this Layer?
**=Transport**

What does TCP stand for?
**=Transmission Control Protocol**

What does UDP stand for?
**=User Datagram Protocol**

What protocol guarantees the accuracy of data?
**=TCP**

What protocol doesn't care if data is received or not by the other device?
**=UDP**

What protocol would an application such as an email client use?
**=TCP**

What protocol would an application that downloads files use?
**=TCP**

What protocol would an application that streams video use?
**=UDP**

What is the name of this layer(5)?
**=Session**

What is the technical term for when a connection is successfully established?
**=Session**

What is the name of this Layer?
**=Presentation**

What is the main purpose that this Layer acts as?
**=Translator**

What is the name of this Layer?
**=Application**

What is the technical term that is given to the name of the software that users interact with?
**=Graphical User Interface**
