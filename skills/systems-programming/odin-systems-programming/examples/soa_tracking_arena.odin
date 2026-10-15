package soa_tracking_arena
import "core:mem"

Particle :: struct { pos: [3]f32, mass: f32 }

integrate_soa :: proc(particles: #soa[]Particle, dt: f32) -> (ok: bool) {
    if dt <= 0 { return false }
    for i in 0..<len(particles) {
        particles[i].pos.x += dt * particles[i].mass
    }
    return true
}
