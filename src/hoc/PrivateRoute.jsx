import React from "react";
import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ children }) => {
	const isActive = useSelector((state) => state.auth.isActive);

	return (
		<>
			{isActive === true && { ...children }}
			{isActive === false && <Navigate to="/sign-in" />}
		</>
	);
};

export default PrivateRoute;
