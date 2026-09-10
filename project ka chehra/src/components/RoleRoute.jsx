import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const RoleRoute = ({ role, children }) => {
  const { user } = useAuth();
  const location = useLocation();
     console.log('RoleRoute check:', { user, expectedRole: role });

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  const userRole = user.role?.roleName?.toUpperCase();

  if (userRole !== role) {
    if (userRole === 'USER') {
      return <Navigate to="/customer/dashboard" replace />;
    } else if (userRole === 'OWNER') {
      return <Navigate to="/owner/dashboard" replace />;
    } else if (userRole === 'ADMIN') {
      return <Navigate to="/admin/dashboard" replace />;
    }
    return <Navigate to="/" replace />;
  }

  return children;
};

export default RoleRoute;