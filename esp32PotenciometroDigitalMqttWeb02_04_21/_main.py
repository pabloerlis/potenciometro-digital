import _thread, mqtt, controllPot, ujson, time, serverfrom nettools import wlan_connect,wlan_disconnect from ws_multiserver import WebSocketMultiServerdef funcMain(topic, msg):  #esta função é chamada quando houver uma msg nova no servidor mqtt  #msg_decode = msg.decode('utf-8')  msg_decode = ujson.loads(msg.decode('utf-8'))  controllPot.controll(msg_decode[0], msg_decode[1])  #topic = 'potenciometroDigital'  #payload = 'teste'  #mqtt.c.publish(topic, payload)  wlan_connect('Senha 123','ang3lica10',timeout=15)mqtt.callback = funcMainmqttStart = _thread.start_new_thread(mqtt.mqtt(),())server.startWeb.start()mqttStart.start() 