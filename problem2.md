Khối $\Omega_2$ được xác định bởi 2 phương trình:

$$
\begin{cases}
    z_1 &= -1 - \cos(\sqrt{x^2 + y^2}) \\
    z_2 &= -\frac{1}{2} - \frac{1}{2}\cos(\sqrt{x^2 + y^2})
\end{cases}
$$

Đổi sang hệ tọa độ trụ:

$$
\begin{cases}
    x &= r\cos(\theta) \\
    y &= r\sin(\theta) \\
    z &= z
\end{cases}
$$

Thay vào phương trình của $\Omega_2$:

$$
\begin{cases}
    z(r, p)_1 = -1 - \cos(r), 0 \leq r \leq \pi , 0 \leq p \leq 2\pi \\
    z(r, p)_2 = -\frac{1}{2} - \frac{1}{2}\cos(r), 0 \leq r \leq \pi , 0 \leq p \leq 2\pi
\end{cases}
$$

Vậy, $-2 \leq z_1 \leq 0$ và $-1 \leq z_2 \leq 0$

$$
\begin{cases}
    r_1 = \cos(-z-1)^{-1} \\
    r_2 = \cos(-2z - 1)^{-1}
\end{cases}
$$

Gọi n là tổng số mặt cắt của mô hình, giả sử n = 10, ta có $\delta z = \frac{2 - 0}{10} = 0.2$, ta có 10 r tương ứng

Dựa vào hình vẽ:

<p align="center">
<img src="./image.png" width="500">
</p>

Ta thấy với $-1 \lt z \leq 0$, mặt cắt là 1 hình vành khăn, nên diện tính được tính bằng công thức: $S = \pi(r_1^2 - r_2^2)$

Tổng diện tích của các lát cắt từ `z = 0` đến `z = -1` là: $P_1 = \sum_{z=0}^{-1} \pi(r_1^2 - r_2^2)$

Với $-2 \lt z \leq -1$, lát cắt là 1 hình tròn, tính bằng công thức: $S = \pi r_1^2$

Tổng diện tích của các lát cắt từ `z = -1` đến `z = -2` là: $P_2 = \sum_{z=-1}^{-2} \pi r_1^2$

Vậy, diện tích các lát cắt của khối $\Omega_2$ là: $S = P_1 + P_2$
