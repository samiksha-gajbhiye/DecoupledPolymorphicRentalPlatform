import * as React from "react";
import { Slot } from "@radix-ui/react-slot";

const Form = React.forwardRef(({ className, children, ...props }, ref) => (
  <form
    ref={ref}
    className={className}
    {...props}
  >
    {children}
  </form>
));
Form.displayName = "Form";

const FormField = React.forwardRef(
  ({ form, name, children, ...props }, ref
) => {
  const [fieldState, setFieldState] = React.useState({});
  const onChange = (value) => {
    setFieldState((prev) => ({ ...prev, value }));
    // Update form value if form controlled
    if (form) {
      form.onChange?.({ target: { name, value } });
    }
  };

  return React.Children.map(children, (child) => {
    if (
      React.isValidElement(child) &&
      child.type.displayName === "FormItem"
    ) {
      return React.cloneElement(child, {
        ...fieldState,
        form,
        name,
        onChange,
        ref,
      });
    }
    return child;
  });
});
FormField.displayName = "FormField";

const FormItem = ({ className, ...props }) => (
  <div className={className} {...props} />
);
FormItem.displayName = "FormItem";

const FormLabel = ({ className, ...props }) => (
  <label className={className} {...props} />
);
FormLabel.displayName = "FormLabel";

const FormControl = ({ className, ...props }) => (
  <div className={className} {...props} />
);
FormControl.displayName = "FormControl";

const FormDescription = ({ className, ...props }) => (
  <p className={className} {...props} />
);
FormDescription.displayName = "FormDescription";

const FormMessage = ({ className, ...props }) => (
  <p className={className} {...props} />
);
FormMessage.displayName = "FormMessage";

export { Form, FormField, FormItem, FormLabel, FormControl, FormDescription, FormMessage };