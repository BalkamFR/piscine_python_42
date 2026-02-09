# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: papilaz <papilaz@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/17 22:11:34 by papilaz           #+#    #+#              #
#    Updated: 2026/01/18 00:20:12 by papilaz          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	create_plant(name, height, age):
	print(name, end=": ")
	print(height, end="cm, ")
	print(age, end=" days old \n")

if __name__ == '__main__':
	create_plant("JBORDELI", 25, 30)
	create_plant("PACOME", 25, 35)
