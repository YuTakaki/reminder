import { createSlice } from "@reduxjs/toolkit";
import { checkAuthenticatedAction, signInAction } from "./actions/authAction";

const initialState = {
	pending: false,
	error: "",
	isActive: null,
	token: "",
	user: {},
};

const authSlicer = createSlice({
	name: "auth",
	initialState,
	reducers: {},
	extraReducers: {
		//checking auth in initial render of app
		[checkAuthenticatedAction.pending]: (state) => {
			state.pending = true;
		},
		[checkAuthenticatedAction.fulfilled]: (state, action) => {
			return {
				...state,
				pending: false,
				...action.payload,
			};
		},
		//checking for login render of app
		[signInAction.pending]: (state) => {
			state.pending = true;
		},
		[signInAction.fulfilled]: (state, action) => {
			return {
				...state,
				pending: false,
				...action.payload,
				error: action.payload.isActive ? "" : action.payload.error,
			};
		},
	},
});
const authReducer = authSlicer.reducer;
export default authReducer;
