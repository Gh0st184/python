from sys import argv

payroll = lambda production, rate, prize: (production * rate) + prize
print(payroll(int(argv[1]), int(argv[2]), int(argv[3])))
