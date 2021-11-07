import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { signInAction } from "../slice/actions/authAction";
import { useNavigate } from "react-router";

const SignIn = () => {
	const dispatch = useDispatch();
	const navigate = useNavigate();
	const [signInForm, setSignInForm] = useState({
		email: "",
		password: "",
	});

	const setSignInFormMethod = (e) => {
		setSignInForm({
			...signInForm,
			[e.target.name]: e.target.value,
		});
	};

	const login = async (e) => {
		try {
			e.preventDefault();
			const action = await dispatch(signInAction(signInForm));
			console.log(action);
			if (!("error" in action.payload)) {
				navigate("../");
			}
		} catch (error) {}
	};

	return (
		<div className="signinPage">
			<main>
				<form onSubmit={login}>
					<input type="text" name="email" onChange={setSignInFormMethod} />
					<input
						type="password"
						name="password"
						onChange={setSignInFormMethod}
					/>
					<input type="submit" />
				</form>
			</main>
		</div>
	);
};

export default SignIn;
