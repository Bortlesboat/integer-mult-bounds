import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Data.Complex.ExponentialBounds
import KappaCheck.Network

/-!
# Certified exponents for the `h = 46` networks

For a network with `W` wires, label dimension `m` and rank sum `s < W m`, the swap /
layer recursions need a rational exponent `τ` with `s / W < m ^ τ` (paper Prop. 11 and
Section 5.3).  Writing `η = 1 - s / (W m)`, it suffices that `(1 - τ) * log m < η`,
because `m ^ (-(1-τ)) = exp (-(1-τ) log m) ≥ 1 - (1-τ) log m`.

We bound `log 97336` from above using only `log 2 < 0.6931471808` (Mathlib) and
`log y ≤ y - 1`:  with `y₀ = 97336 / 2^17` and `q^256 ≥ y₀`,
`log 97336 = 17 log 2 + log y₀ ≤ 17 log 2 + 256 (q - 1)`.
-/

namespace KappaCheck.Certificates

open Real

/-- rational upper bound for `log 97336` (true value `11.48592…`) -/
def L0 : ℚ := 17 * (6931471808 / 10 ^ 10) + 256 * (249709565437 / 250000000000 - 1)

theorem log_m_lt : Real.log 97336 < (L0 : ℝ) := by
  have hq : ((97336 : ℝ) / 2 ^ 17) ≤ ((249709565437 : ℝ) / 250000000000) ^ 256 := by
    norm_num
  have hy : Real.log ((97336 : ℝ) / 2 ^ 17) ≤ 256 * ((249709565437 : ℝ) / 250000000000 - 1) := by
    calc Real.log ((97336 : ℝ) / 2 ^ 17)
        ≤ Real.log (((249709565437 : ℝ) / 250000000000) ^ 256) :=
          Real.log_le_log (by norm_num) hq
      _ = 256 * Real.log ((249709565437 : ℝ) / 250000000000) := by
          rw [Real.log_pow]; norm_num
      _ ≤ 256 * ((249709565437 : ℝ) / 250000000000 - 1) := by
          gcongr; exact Real.log_le_sub_one_of_pos (by norm_num)
  have h2 : Real.log 2 < 0.6931471808 := Real.log_two_lt_d9
  norm_num at h2
  have hsplit : Real.log 97336 = 17 * Real.log 2 + Real.log ((97336 : ℝ) / 2 ^ 17) := by
    rw [Real.log_div (by norm_num) (by norm_num), Real.log_pow]; push_cast; ring
  rw [hsplit]
  unfold L0; push_cast
  linarith

/-- General certificate: if `x > 0`, `x * L ≤ η`, `log m < L`, `m > 0` and
`r = m (1 - η)`, then `r < m ^ (1 - x)`. -/
theorem exponent_certificate (m L x η r : ℝ) (hm : 0 < m) (hx : 0 < x)
    (hlog : Real.log m < L) (hxη : x * L ≤ η) (hr : r = m * (1 - η)) :
    r < m ^ (1 - x) := by
  have hpow : m ^ (1 - x) = m * Real.exp (-(Real.log m * x)) := by
    rw [Real.rpow_sub hm, Real.rpow_one, Real.rpow_def_of_pos hm, Real.exp_neg, div_eq_mul_inv]
  have hexp := Real.add_one_le_exp (-(Real.log m * x))
  have h1 : Real.log m * x < L * x := mul_lt_mul_of_pos_right hlog hx
  have h3 : 1 - η < Real.exp (-(Real.log m * x)) := by nlinarith
  rw [hpow, hr]
  exact mul_lt_mul_of_pos_left h3 hm

/-- `1 - τ` for the bit network (`h = 46`) -/
def xb : ℚ := 5189625 / 2 ^ 58
/-- `1 - σ` for the complex network (`h = 46`) -/
def yc : ℚ := 986667 / 2 ^ 55

open KappaCheck.Network in
/-- The bit network with `h = 46` satisfies `s_b / W_b < m ^ τ` with `τ = 1 - xb`. -/
theorem bit_exponent :
    ((sb 46 : ℕ) : ℝ) / (Wb 46 : ℕ) < (97336 : ℝ) ^ (1 - (xb : ℝ)) := by
  obtain ⟨-, -, -, hsb, -, -⟩ := new_h46
  obtain ⟨-, -, hWb, -, -, -⟩ := new_h46
  rw [hsb, hWb]
  apply exponent_certificate 97336 (L0 : ℝ) (xb : ℝ) (9 / 43518487588) _ (by norm_num)
    (by unfold xb; norm_num) log_m_lt
  · unfold xb L0; norm_num
  · norm_num

open KappaCheck.Network in
/-- The complex network with `h = 46` satisfies `s_c / W_c ≤ m ^ σ` with `σ = 1 - yc`. -/
theorem complex_exponent :
    ((sc 46 : ℕ) : ℝ) / (Wc 46 : ℕ) < (97336 : ℝ) ^ (1 - (yc : ℝ)) := by
  obtain ⟨-, -, -, -, hWc, hsc⟩ := new_h46
  rw [hsc, hWc]
  apply exponent_certificate 97336 (L0 : ℝ) (yc : ℝ)
    (1 - (12737958894652805035200 : ℝ) / 130865855373752400 / 97336) _ (by norm_num)
    (by unfold yc; norm_num) log_m_lt
  · unfold yc L0; norm_num
  · ring

/-- the complex exponent is strictly smaller than the bit exponent (`σ < τ`) -/
theorem sigma_lt_tau : (1 - (yc : ℝ)) < 1 - (xb : ℝ) := by
  unfold yc xb; norm_num

end KappaCheck.Certificates
