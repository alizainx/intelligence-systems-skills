function x = damped_least_squares(A, b, lambda) %#codegen
    arguments
        A (:,:) double {mustBeFinite, mustBeNonEmpty}
        b (:,1) double {mustBeFinite}
        lambda (1,1) double {mustBePositive}
    end
    [m, n] = size(A);
    if size(b, 1) ~= m
        error('ISS:DimensionMismatch', 'Row count of A (%d) must match length of b (%d).', m, size(b, 1));
    end
    % Solve (A'*A + lambda^2 * I) * x = A'*b via augmented QR backslash (never inv())
    aug_A = [A; lambda * eye(n, 'like', A)];
    aug_b = [b; zeros(n, 1, 'like', b)];
    x = aug_A \ aug_b;
end
