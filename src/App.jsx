import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PrivateRoute from "./hoc/PrivateRoute";
import Home from "./pages/Home";
import SignIn from "./pages/SignIn";
import { checkAuthenticatedAction } from "./slice/actions/authAction";

function App() {
	const dispatch = useDispatch();
	useEffect(() => {
		dispatch(checkAuthenticatedAction());
	}, []);
	return (
		<div className="App">
			<BrowserRouter>
				<Routes>
					<Route
						path="/"
						element={
							<PrivateRoute>
								<Home />
							</PrivateRoute>
						}
					/>
					<Route path="/sign-in" element={<SignIn />} />
				</Routes>
			</BrowserRouter>
		</div>
	);
}

export default App;
