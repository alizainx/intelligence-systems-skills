module TypeStableStencil
export step_1d_heat!

struct Grid1D{T<:AbstractFloat}
    u::Vector{T}
    u_next::Vector{T}
    alpha::T
end

function step_1d_heat!(g::Grid1D{T}) where {T<:AbstractFloat}
    u, un, a = g.u, g.u_next, g.alpha
    n = length(u)
    length(un) == n || throw(DimensionMismatch("Buffer size mismatch"))
    @inbounds for i in 2:(n - 1)
        un[i] = u[i] + a * (u[i - 1] - T(2) * u[i] + u[i + 1])
    end
    return un
end
end # module
