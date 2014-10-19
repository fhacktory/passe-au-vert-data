function isReachable(s_start, v_start, s_target, t_left) {
    // Return if the target is reachable in the alloted time t_left.

    // We start by computing the furthest we could go.
    // We have 2 phases: phase 1 is acceleration, phase 2 is max speed.
    t_acc_max = 2 * (V_MAX - v_start) / ACC;
    s_max_phase_1 = s_start + t_acc_max * v_start + 0.5 * ACC * (t_acc_max ** 2);
    s_max_phase_2 = s_max_phase_1 + Math.max(t_left - t_acc_max, 0) * V_MAX;

    // We compare it to our target.
    if (s_max_phase_2 > s_target) {
        return true;
    } else {
        return false;
    }
}
