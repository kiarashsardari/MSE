# MSE / RMSE

محاسبهٔ Mean Squared Error و Root Mean Squared Error بین دو تابع، همراه با نمایش نمودار.

## توابع

### `truth(x)`
تابع مرجع (مقدار واقعی):
```python
truth(x) = 2x² + 3
```

### `guess(x)`
تابع تقریب (مقدار پیش‌بینی‌شده):
```python
guess(x) = 2x² − 4
```

### `mse(y_true, y_pred)`
میانگین مربعات خطا را حساب می‌کند:

```
MSE = Σ(y_true − y_pred)² / n
```

ورودی‌ها آرایه‌های numpy هستند و محاسبه به‌صورت vectorized انجام می‌شود.

### `rmse(mse_value)`
جذر MSE را برمی‌گرداند:

```
RMSE = √MSE
```

### `plot_functions(f_true, f_pred)`
دو تابع را روی بازهٔ `[1, 10]` با ۱۰۰ نقطه رسم می‌کند.

## مثال

```python
x_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_true = truth(x_list)
y_pred = guess(x_list)

print(rmse(mse(y_true, y_pred)))   # 7.0
plot_functions(truth, guess)
```

## خروجی

```
7.0
```

چون اختلاف دو تابع ثابت است:

```
truth(x) − guess(x) = (2x² + 3) − (2x² − 4) = 7
```

پس:

- MSE = 49
- RMSE = 7

## پیش‌نیاز

```bash
pip install numpy matplotlib
```

## اجرا

```bash
python MSE.py
```

## نکات

- محاسبهٔ MSE روی آرایه‌های numpy انجام می‌شود (vectorized).
- `len(y_true)` به‌عنوان `n` استفاده می‌شود.
- توابع `truth` و `guess` فقط نمونه هستند؛ می‌توانید هر تابع دلخواهی جای‌گزین کنید.
- برای مشاهدهٔ خطا در نمودار، می‌توانید تفاضل دو تابع را هم رسم کنید.
