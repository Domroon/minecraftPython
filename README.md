# Hilfe Links

- bukkit herunterladen und kompilieren (https://www.spigotmc.org/wiki/buildtools/)
- bukkit plugin herunterladen (https://github.com/zhuowei/RaspberryJuice)
- python modul mit pip installieren (https://pypi.org/project/mcpi/)
- mcpi API: https://www.stuffaboutcode.com/p/minecraft-api-reference.html

# Startbereitschaft herstellen

- bukkit server starten
- minecraft client auf version 1.19.2 starten

# Python benutzen

- python repl starten und "mcpi" importieren
- python script mit der bibliothek "mcpi" starten
- hier folgen vorgeschlagene Dinge, welche man in minecraft mit python tun könnte

# Spigot Version 1.19 mit RaspberryJuice

1. Java installieren
2. Build tool herunterladen und in vorgesehenen ordner verschrieben: https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
3. java -jar BuildTools.jar --rev latest im Ordner ausführen
4. apache-maven-3.6.0/bin zum windows PATH hinzufügen
5. Spigot server plugin herunterladen: git clone https://github.com/zhuowei/RaspberryJuice
6. Im RaspberryJuice ordner mvn package ausführen
7. Spigot server einmalig mithilfe des folgenden batch-scripts starten (und auch sonst damit starten):
   @echo off
   java -Xms1G -Xmx1G -XX:+UseG1GC -jar spigot-1.19.2.jar nogui
   pause
8. Nun erzeugte java-datei im ordner “target” in den plugin ordner von spigot verschieben
9. Mincraft in der Version 1.19 starten
10. Python kann nun mithilfe des moduls “mcpi” befehle an den server schicken

# Blöcke setzen

mc.setBlock(x+2, y, z, mcpi.block.DIAMOND_BLOCK.id, 0)

## Konstanten

Siehe hier: https://github.com/martinohanlon/mcpi/blob/master/mcpi/block.py

## Geplante Funktionen

- [ ] jeden Block direkt vor Spieler generieren
