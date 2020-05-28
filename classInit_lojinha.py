# cafe store ex

produtos = {
	1: {'nome':'cookie', 'peso':50, 'estoque':152, 'preço':5.}, 
	2: {'nome':'cookie de tamara', 'peso':50, 'estoque':152, 'preço':5.},
	3: {'nome':'cookie de pistache', 'peso':50, 'estoque':152, 'preço':5.},
	4: {'nome':'cookie ouro', 'peso':50, 'estoque':152, 'preço':2500.},
	5: {'nome':'cookie light', 'peso':50, 'estoque':152, 'preço':5.},
}

clientes = [
	 {'nome':'cookie'}, 
	 {'nome':'cookie de tamara'},
	 {'nome':'cookie de pistache'},
	 {'nome':'cookie ouro'},
	 {'nome':'cookie light'},
]


pedidos = []


pedidos.append({'numero':1001, 'itens':[{'produto':2, 'qnt':152}], 'cliente':'Lady'})
pedidos.append({'numero':1002, 'itens':[{'produto':5, 'qnt':152}], 'cliente':'Dude'})
pedidos.append({'numero':1003, 'itens':[{'produto':2, 'qnt':152}], 'cliente':'Du'})
pedidos.append({'numero':1004, 'itens':[{'produto':3, 'qnt':152}], 'cliente':'Dudu'})
pedidos.append({'numero':1005, 'itens':[{'produto':5, 'qnt':152}], 'cliente':'Edu'})


for pedido in pedidos:
	nome_do_cliente = pedido['cliente']
	peso_total = 0
	preço_total = 0
	for item in pedido['itens']:
		id_do_produto = item['produto']
		quantidade_do_produto = item['qnt']
		produto = produtos[id_do_produto]
		peso_individual = quantidade_do_produto * produto['peso']
		preço_individual = quantidade_do_produto * produto['preço']
		preço_total = preço_total + preço_individual  
		peso_total = peso_total + peso_individual
	print(f'Cliente {nome_do_cliente} - 0 peso do pedido e {peso_total}, e o preço do pedido e {preço_total}')