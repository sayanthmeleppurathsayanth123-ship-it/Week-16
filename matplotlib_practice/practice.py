import matplotlib.pyplot as plt

# x= [0, 1, 2, 3, 4]
# y= [0, 1, 4, 9, 16]
# plt.plot(x,y)
# plt.show()

x= [0, 2, 4, 6, 8]
y= [0, 4, 16, 36, 64]

fig, ax=plt.subplots()
ax.plot(x,y, marker="o", label="Data Points")

ax.set_title("Basic components of matplotlib figure")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

plt.show()