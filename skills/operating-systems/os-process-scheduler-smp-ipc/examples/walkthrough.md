# Verified Example: `os-process-scheduler-smp-ipc` (`cfs_scheduler.c`)

```
#include <assert.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    uint32_t tid;
    uint32_t weight;
    uint64_t vruntime_ns;
    bool runnable;
} cfs_task_t;

/* Picks runnable task with minimum virtual runtime (CFS fairness invariant)
 * and advances its vruntime by delta_exec * (NICE_0_WEIGHT / weight).
 */
static int cfs_schedule_tick(cfs_task_t *tasks, size_t n, uint64_t delta_ns, uint32_t *out_tid) {
    size_t best_idx = n;
    for (size_t i = 0U; i < n; ++i) {
        if (tasks[i].runnable && (best_idx == n || tasks[i].vruntime_ns < tasks[best_idx].vruntime_ns)) {
            best_idx = i;
        }
    }
    if (best_idx == n) return -1;
    *out_tid = tasks[best_idx].tid;
    tasks[best_idx].vruntime_ns += (delta_ns * 1024ULL) / (uint64_t)tasks[best_idx].weight;
    return 0;
}

int main(void) {
    cfs_task_t runq[2] = {
        {.tid = 1U, .weight = 1024U, .vruntime_ns = 0ULL, .runnable = true},
        {.tid = 2U, .weight = 2048U, .vruntime_ns = 0ULL, .runnable = true} /* 2x weight -> vruntime grows half as fast */
    };
    uint32_t picked = 0U;
    uint32_t count_t1 = 0U, count_t2 = 0U;
    for (int step = 0; step < 30; ++step) {
        assert(cfs_schedule_tick(runq, 2U, 1000ULL, &picked) == 0);
        if (picked == 1U) count_t1++;
        if (picked == 2U) count_t2++;
    }
    /* Task 2 (weight 2048) must receive exactly 2x CPU slices (20 vs 10) as Task 1 (weight 1024)! */
    assert(count_t1 == 10U && count_t2 == 20U);
    puts("OS CFS PROPORTIONAL-SHARE SCHEDULER VERIFIED (20:10 slice ratio)");
    return 0;
}

```
